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
from utils import check_duplicate, DuplicatedEntryError, AuthenticationError

class SignUpView(View):
    # Limit HTTP methods to POST
    http_method_names = ["post"]

    def post(self, request):

        try:
            # load data from request body
            data = json.loads(request.body)

            # Validate Email and Password
            validate_email(data["email"])
            validate_password(data["password"])

            # Check if unique field duplicated
            check_duplicate(User, data)

            # Create User Data
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

        except IntegrityError as e:
            return JsonResponse(
                {
                    "message": "DataBase Integrity Error: {}".format(str(e.__cause__)),
                },
                status=500,
            )

        else:
            return JsonResponse(
                {
                    "message": "SUCCESS",
                    "user": user.to_dict(),
                },
                status=200
            )

class SignInView(View):
    # Limit Http Method to POST
    http_method_names = ["post"]

    def post(self, request):
        
        try:
            # loads data from request body
            data = json.loads(request.body)

            # access required fields
            email = data['email']
            password = data['password']

            # check if user exists
            user = User.objects.get(email=email)

            # check if password matches
            if user.password != str(password):
                raise AuthenticationError

        except JSONDecodeError as e:
            return JsonResponse({"message": e.msg}, status=400)
        
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)
        
        except User.DoesNotExist:
            return JsonResponse({"message": "INVALID_USER"}, status=401)

        except AuthenticationError:
            return JsonResponse({"message": "INVALID_USER"}, status=401)

        else:
            return JsonResponse({"message": "SUCCESS"}, status=200)