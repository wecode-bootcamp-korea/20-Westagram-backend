import json

from django.http  import JsonResponse
from django.views import View

from user.models   import User
from user.validate import validate_email, validate_password

class signupView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            if not validate_email(data['email']):
                return JsonResponse({'message':'INVALID EMAIL'}, status=400)

            if not validate_password(data['password']):
                return JsonResponse({'message':'INVALID PASSWORD'}, status=400)

            if User.objects.filter(email=data['email']).exists():
                return JsonResponse({'message':'DUPLICATE EMAIL'}, status=409)

            User.objects.create(
                    email         = data['email'], 
                    password      = data['password'],
                    phone_number  = data.get('phone_number'),
                    nickname      = data.get('nickname')
                )
            return JsonResponse({'message': 'SUCCESS'})
        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)

class loginView(View):
    def post(self, request):
        data = json.loads(request.body)

        log_email    = data.get('email')
        log_password = data.get('password')

        if not log_email or not log_password:
            return JsonResponse({"message":"KEY_ERROR"}, status=400)
        
        if not User.objects.filter(email=log_email).exists():
            return JsonResponse({"message":"INVALID_USER"}, status=401)

        if not User.objects.get(email=log_email).password == log_password:
            return JsonResponse({"message":"INVALID_PASSWORD"}, status=401)
        
        return JsonResponse({"message":"SUCCESS"}, status=200)