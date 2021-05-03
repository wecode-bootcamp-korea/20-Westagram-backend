import json

from django.http  import JsonResponse
from django.views import View

from user.models   import User
from user.validate import *


class signupView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            if not validate_email(data['email']):
                return JsonResponse({'message':'INVALID EMAIL'}, status=400)
            if not validate_password(data['password']):
                return JsonResponse({'message':'INVALID PASSWORD'}, status=400) 
            if not duplicate_email(data['email']):
                return JsonResponse({'message':'DUPLICATE EMAIL'}, status=409)

            User.objects.create(
                    email         = data['email'], 
                    password      = data['password'],
                    phone_number  = data['phone_number'],
                    nickname      = data['nickname']
                )
            return JsonResponse({'message': 'SUCCESS'})
        except:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)


class loginView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            log_email    = data['email']
            log_password = data['password']
            email = User.objects.get(user_email = log_email)
            
            if email.user_password == log_password:
                return JsonResponse({"message":"SUCCESS"}, status=200)
            else:
                return JsonResponse({"message":"INVALID_USER"}, status=401)

        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)
        except:
            return JsonResponse({'message':'INVALID_USER'}, status=401)
