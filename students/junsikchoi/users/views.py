import json
import time
import bcrypt
import jwt
from json                   import JSONDecodeError

from django.db              import IntegrityError
from django.views           import View
from django.http            import JsonResponse
from django.core.exceptions import ValidationError

from users.models           import User
from users.validators       import validate_email, validate_password
from utils                  import check_duplicate, DuplicatedEntryError, AuthenticationError
from my_settings            import JWT_SECRET_KEY, JWT_ALGORITHM, JWT_DURATION_SEC

class SignUpView(View):

    def post(self, request):

        try:
            data = json.loads(request.body)

            validate_email(data["email"])
            validate_password(data["password"])
            
            check_duplicate(User, data)

            hashed_password = bcrypt.hashpw(data.get('password').encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

            user = User.objects.create(
                email = data.get('email'),
                password = hashed_password,
                username = data.get('username'),
                phone_number = data.get('phone_number'),
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

class SignInView(View):

    def post(self, request):
        
        try:
            if request.headers.get('Authorization'):
                token = request.headers.get('Authorization')
                payload = jwt.decode(token, JWT_SECRET_KEY, JWT_ALGORITHM)
                user = User.objects.get(pk=payload.get('user_id'))
            
            else:
                data = json.loads(request.body)

                email = data['email']
                password = data['password']

                user = User.objects.get(email=email)

                if not bcrypt.checkpw(data.get('password').encode('utf-8'),user.password.encode('utf-8')):
                    return JsonResponse({"result": "INVALID_USER"}, status=401)

            new_token = jwt.encode({'user_id': user.id, 'iat': int(time.time()), 'exp': int(time.time()) + JWT_DURATION_SEC}, 
                                JWT_SECRET_KEY, 
                                JWT_ALGORITHM)

            return JsonResponse({"result": "SUCCESS", "token": new_token}, status=200)

        except JSONDecodeError as e:
            return JsonResponse({"result": "JSON_DECODE_ERROR", "message": e.msg}, status=400)
        
        except jwt.exceptions.ExpiredSignatureError as e:
            return JsonResponse({"result": "TOKEN_ERROR", "message": e.args[0]})
        
        except jwt.exceptions.InvalidSignatureError as e:
            return JsonResponse({"result": "TOKEN_ERROR", "message": e.args[0]})
        
        except jwt.exceptions.DecodeError as e:
            return JsonResponse({"result": "TOKEN_ERROR", "message": e.args[0]})

        except KeyError as e:
            return JsonResponse({"result": "KEY_ERROR", "message": f'Key Error in Field "{e.args[0]}"'}, status=400)
        
        except User.DoesNotExist:
            return JsonResponse({"result": "INVALID_USER"}, status=401)