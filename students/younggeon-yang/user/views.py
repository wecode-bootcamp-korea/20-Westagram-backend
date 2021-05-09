import json
import jwt
import bcrypt
from json.decoder     import JSONDecodeError

from django.http      import JsonResponse
from django.views     import View

from user.models      import User
from user.validations import Validation
from my_settings      import SECRET_KEY

class SignUpView(View):
    def post(self, request):
        try:
            data     = json.loads(request.body)
            email    = data['email']
            password = data['password']

            phone    = data.get('phone', None)  
            nickname = data.get('nickname', None)
            phone    = None if not phone else phone  
            nickname = None if not nickname else nickname

            if not Validation.validate_email(self, email):
                return JsonResponse({'message': 'Error email'}, status=400)

            if not Validation.validate_password(self, password):
                return JsonResponse({'message': 'Error password'}, status=400)

            if not Validation.validate_duplication(self, email, phone, nickname):
                return JsonResponse({'message': 'Already exist'}, status=400)


            password = bcrypt.hashpw(
                    password.encode('utf-8'),
                    bcrypt.gensalt()
            ).decode('utf-8')
            User.objects.create(email=email, password=password, phone=phone, nickname=nickname)

            return JsonResponse({'message': 'Success'}, status=201)
        except KeyError:
            return JsonResponse({'message': 'No keyword'}, status=400)
        except JSONDecodeError:
            return JsonResponse({'message': 'No body'}, status=400)

class LoginView(View):
    def post(self, request):
        try:
            data     = json.loads(request.body)
            email    = data.get('email', None)
            phone    = data.get('phone', None)
            nickname = data.get('nickname', None)

            if email:
                password_db = User.objects.filter(email=email).first().password
                user = User.objects.get(email=email)
            elif phone:
                password_db = User.objects.filter(phone=phone).first().password
                user = User.objects.get(phone=phone)
            elif nickname:
                password_db = User.objects.filter(nickname=nickname).first().password
                user = User.objects.get(nickname=nickname)
            else:
                return JsonResponse({'message': 'No account input'}, status=400)

            if not bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')):
                return JsonResponse({'message': 'Wrong password'}, status=401)

            access_token = jwt.encode(
                    {'user.id': user.id},
                    SECRET_KEY,
                    algorithm = 'HS256'
            )

            return JsonResponse({'message': 'SUCCESS', 'ACCESS_TOKEN': access_token}, status=200)
        except KeyError:
            return JsonResponse({'message': 'No keyword'}, status=400)
        except JSONDecodeError:
            return JsonResponse({'message': 'No body'}, status=400)
        except AttributeError:
            return JsonResponse({'message': 'No account name'}, status=401)
