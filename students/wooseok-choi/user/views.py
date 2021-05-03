import json
import re

from django.http  import JsonResponse
from django.views import View

from user.models import User

def validate_email(email):
    regex = re.compile('^[a-z0-9+-_.]+@[a-z0-9-]+\.[a-z0-9-.]+$', re.I)
    match = regex.match(str(email))
    return bool(match)

def validate_password(password):
    regex = re.compile('^[a-z0-9_-]{8,16}$', re.I)
    match = regex.match(str(password))
    return bool(match)

class signupView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            if not validate_email(data['email']):
                return JsonResponse({'MESSAGE':'INVALID EMAIL'}, status=400)
            if not validate_password(data['password']):
                return JsonResponse({'MESSAGE':'INVALID PASSWORD'}, status=400) 

            User.objects.create(
                    email         = data['email'], 
                    password      = data['password'],
                    phone_number  = data['phone_number'],
                    nickname      = data['nickname']
                )
        except:
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=400)

        return JsonResponse({'MESSAGE': 'SUCCESS'}, status=201)


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
