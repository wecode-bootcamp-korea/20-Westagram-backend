import json
from json                   import JSONDecodeError
import bcrypt

from django.db              import IntegrityError
from django.views           import View
from django.http            import JsonResponse
from django.core.exceptions import ValidationError

from users.models           import User
from users.validators       import validate_email, validate_password
from utils                  import check_duplicate, DuplicatedEntryError

class SignUpView(View):

    def post(self, request):

        try:
            data = json.loads(request.body)

            validate_email(data["email"])
            validate_password(data["password"])
            
            check_duplicate(User, data)

            hashed_password = bcrypt.hashpw(data.get('password').encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

            user = User.objects.create(
                email          = data.get('email'),
                password       = hashed_password,
                username       = data.get('username'),
                phone_number   = data.get('phone_number'),
            )

            return JsonResponse({ "result": "SUCCESS", "user": user.to_dict()}, status=200)

        except JSONDecodeError as e:
            return JsonResponse({"result": "JSON_DECODE_ERROR", "message": e.msg}, status=400)

        except ValidationError as e:
            return JsonResponse({"result": "INVALID_DATA_ERROR", "message": e.message}, status=400)

        except KeyError as e:
            return JsonResponse({"result": "KEY_ERROR", "message": f'Key Error in Field "{e.args[0]}"'}, status=400)

        except DuplicatedEntryError as e:
            return JsonResponse({"result": "DUPLICATED_ENTRY", "message": e.err_message}, status=409)