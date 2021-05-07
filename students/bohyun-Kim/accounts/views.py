

# Create your views here.
import json
<<<<<<< HEAD
import jwt
=======
>>>>>>> e629932b01ab9d3fee4377c9a6a5295bd3b1c16a
import re

from django.http     import JsonResponse
from django.views    import View
<<<<<<< HEAD
from django.conf     import settings
=======
>>>>>>> e629932b01ab9d3fee4377c9a6a5295bd3b1c16a
from accounts.models import User

class AccountView(View):
    def get(self, request):
        pass

    def post(self, request):
        data = json.loads(request.body)

        email = data["email"]
        password = data["password"]
        phone_number = data["phone_number"]
        user_name = data["user_name"]
        
        if not ('email' in data.keys() or 'password' in data.keys()):
            return JsonResponse({'MESSAGE': 'KEY_ERROR'}, status=400)
        if not ('@' in email and '.' in email):
            return JsonResponse({'MESSAGE':'INVALID EMAIL'}, status=400)
        if len(password) < 8:
            return JsonResponse({'MESSAGE':'INVALID PASSWORD'}, status=400)
        
        if (
            User.objects.filter(email=email).exists()
            or User.objects.filter(user_name=user_name).exists()
            or User.objects.filter(phone_number=phone_number).exists()
        ):
            return JsonResponse({'MESSAGE':'EXISTING USER DATA'}, status=400)

        
        User.objects.create(
            email=data['email'],
            phone_number=data['phone_number'],
            user_name=data['user_name'],
            password=data['password'],
        )
        

        return JsonResponse({'MESSAGE':'SUCCESS'}, status=201)


class LoginView(View):
    def post(self, request):
        data = json.loads(request.body)

        email = data["email"]
        password = data["password"]

        if not ('email' in data.keys() or 'password' in data.keys()):
            return JsonResponse({'MESSAGE': 'KEY_ERROR'}, status=400)

        if (
            not ('@' in email and '.' in email)
            or not User.objects.filter(email=email).exists()
            or not User.objects.filter(email=email, password=password).exists():
        ):
                return JsonResponse({'MESSAGE': 'INVALID_USER'}, status=401)
       
        user = User.objects.filter(email=email)[0]
        payload = {"email": user["email"], "user_name": user["user_name"]}
        login_token = jwt.encode(payload, settings.SECRET_KEY, 'HS256')
        return JsonResponse({'MESSAGE': 'SUCCESS', 'LOGIN_TOKEN': login_token}, status=200)
