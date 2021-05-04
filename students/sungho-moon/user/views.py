from django.shortcuts import render

# Create your views here.

import json

from django.http import JsonResponse
from django.views import View

from user.models import Signin


class SigninView(View):
    
    def post(self, request):
        data=json.loads(request.body)

        signin_email   = data['email']
        signin_password= data['password']

        if not signin_email and not signin_password:
            return JsonResponse({"messege":"KEYERROR"}, status=400)
        elif not Signup.objects.filter(email=signin_email).exist() :
            return JsonResponse({'messege":"INVALID_EMAIL'}, status=400)
        elif not Signup.objects.get(email=signin_email).password == signin_password:
            return JsonResponse({"messege":"INVALID_PASSWORD"}, status=400)
        else: return JsonResponse({"messege":"SUCCESS"}, status=200)

        
       