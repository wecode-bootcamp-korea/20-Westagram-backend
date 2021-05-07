

# Create your views here.
import json
import re

from django.http     import JsonResponse
from django.views    import View
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


class AuthView(View):
    def post(self, request):
        pass