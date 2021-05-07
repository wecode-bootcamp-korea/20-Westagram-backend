import json
import bcrypt
import jwt

from django.views   import View
from django.http    import JsonResponse
from account.models import User
class SignupViews(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            email        = data['email']
            password     = data['password']
            phone_number = data.get('phone_number')
            nickname     = data.get('nickname')
            
            if email == "" or password == "":
                return JsonResponse({'MESSAGE':'KEY_ERROR'}, status = 400)

            if data['email'].count('@') == 0 or data['email'].count('.') == 0:
                return JsonResponse({'MESSAGE' : 'KEY_ERROR'}, status = 400) 

            if User.objects.filter(phone_number=data.get('phone_number')).exists()\
                and data.get('phone_number') != None:
                return JsonResponse({'MESSAGE': 'ALREADY_EXISTS'}, status = 400)

            if User.objects.filter(nickname=data.get('nickname')).exists()\
                and data.get('nickname') != None:
                return JsonResponse({'MESSAGE' : 'ALREADY_EXISTS'}, status = 400)

            if User.objects.filter(email=data['email']).exists():\
                return JsonResponse({"MESSAGE" : 'ALREADY_EXISTS'}, status = 400)

            PASSWORD_LENGTH = 8
            if len(data['password']) < PASSWORD_LENGTH:
                return JsonResponse({'MESSAGE' : 'INVALID_PASSWORD'}, status = 400)
            
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8') 

            User.objects.create(
                email         = email,
                password      = hashed_password,
                nickname      = nickname,
                phone_number  = phone_number
            )

            return JsonResponse({'Message' : 'SUCCESS'}, status = 201)
        except KeyError:
            return JsonResponse({'MESSAGE' : 'KEY_ERROR'}, status = 400)

class SigninViews(View):
    def post(self, request):
        try:
            data         = json.loads(request.body)
            email        = data['email']
            password     = data['password']
            
            if not User.objects.filter(email=email).exists():
                return JsonResponse({"MESSAGE" : "INVALID_USER"}, status=400)
            
            user = User.objects.get(email=email)
                
            if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                token = jwt.encode({'user_id' : user.id}, 'secret', algorithm = 'HS256')
                return JsonResponse({"TOKEN" : token, "MESSAGE" : "SUCCESS!"}, status=200)
            else:
                return JsonResponse({"MESSAGE" : "INVALID_USER"}, status=400)

        except KeyError:
            return JsonResponse({"MESSAGE" : "KEY_ERROR"}, status=400)