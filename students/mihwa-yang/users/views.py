import json

from django.http  import JsonResponse
from django.views import View

from users.models import User

class SignUpView(View): 
    def post(self, request):
        data  = json.loads(request.body)
        nickname = data.get('nickname')

        if 'password' not in data.keys() or 'email' not in data.keys():
            return JsonResponse({"MESSAGE": "KEY ERROR"}, status=400)

        if data['email'].count('@') == 0 or data['email'].count('.') == 0:
            return JsonResponse({"MESSAGE": "EMAIL FORM ERROR"}, status=400)
        
        PASSWORD_LENGTH = 8 
        if len(data['password']) < PASSWORD_LENGTH:
            return JsonResponse({"MESSAGE": "PASSWORD ERROR"}, status=400)

        if User.objects.filter(email=data.get('email')).exists():
            return JsonResponse({"MESSAGE": "ALREADY EXIT ERROR"}, status=400)

        if User.objects.filter(nickname=data.get('nickname')).exists() \
            and User.objects.filter(nickname=data.get('nickname') is not None):
            return JsonResponse({"MESSAGE": "ALREADY EXIT ERROR"}, status=400)

        if User.objects.filter(phone=data.get('phone')).exists() \
            and User.objects.filter(phone=data.get('phone') is not None):
            return JsonResponse({"MESSAGE": "ALREADY EXIT ERROR"}, status=400)
            
        User.objects.create(
            email    = data.get('email'),
            password = data.get('password'),
            nickname = data.get('nickname'),
            phone    = data.get('phone')
        )
        return JsonResponse({'MESSAGE':'SIGNUP SUCCESS'}, status=201)


class SignInView(View): 
    def post(self, request):
        data  = json.loads(request.body)

        if 'email' not in data.keys() or 'password' not in data.keys():
            return JsonResponse({"MESSAGE": "KEY ERROR"}, status=400)

        if User.objects.filter(email=data['email']).exists() == False:
            return JsonResponse({"MESSAGE": "INVALID USER"}, status=401)

        if data['password'] != User.objects.get(email=data['email']).password:
            return JsonResponse({"MESSAGE": "INVALID USER"}, status=401)
        
        if User.objects.filter(email=data['email'], password=data['password']).exists():
            return JsonResponse({"MESSAGE": "SUCCESS"}, status=200)