import json
from json import JSONDecodeError
from django.db import IntegrityError
from django.views import View
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from users.models import User
from users.validators import (
    validate_email,
    validate_password,
)
from utils import check_duplicate, DuplicatedEntryError

class SignUpView(View):

    def post(self, request):

        try:
            data = json.loads(request.body)

            validate_email(data["email"])
            validate_password(data["password"])
            
            check_duplicate(User, data)

            user = User.objects.create(
                email = data.get('email'),
                password = data.get('password'),
                username = data.get('username'),
                phone_number = data.get('phone_number'),
            )

        except JSONDecodeError as e:
            return JsonResponse({"message": e.msg}, status=400)

        except ValidationError as e:
            return JsonResponse({"message": e.message}, status=400)

        except KeyError as e:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)

        except DuplicatedEntryError as e:
            return JsonResponse({"message": e.err_message}, status=409)

        else:
            return JsonResponse(
                {
                    "message": "SUCCESS",
                    "user": user.to_dict(),
                },
                status=200
            )
