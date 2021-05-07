import json, re

from django.views             import View
from django.http              import JsonResponse
from django.core.exceptions   import ValidationError

from .models                  import User


class SignupView(View):
    def post(self, request):
        data      = json.loads(request.body)
        email_reg = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        regex     = re.compile(email_reg)

        try:
            if not regex.match(data['email']):
                return JsonResponse ({"message": "This email is not valid"}, status=400)

            if len(data['password']) < 8:
                 return JsonResponse ({"message": "This password is too short"}, status=400)

            if User.objects.filter(email = data['email']).exists():
                return JsonResponse ({"message": "This email already exists."}, status=400)

            if data.get('nickname') != None and User.objects.filter(nickname = data['nickname']).exists():
                    return JsonResponse ({"message": "This nickname already exists."}, status=400)

            if data.get('phone_number') != None and User.objects.filter(phone_number = data['phone_number']).exists():
                    return JsonResponse ({"message": "This phone_number already exists."}, status=400)

            else:
                User.objects.create(
                        email        = data.get('email'),
                        password     = data.get('password'),
                        nickname     = data.get('nickname'),
                        phone_number = data.get('phone_number')
                    )
                return JsonResponse ({"message": "SUCCESS"}, status=200)

        except KeyError:
            return JsonResponse({"message" : 'KEY_ERROR'}, status=400)

class SigninView(View):
    def post(self, request):
        data     = json.loads(request.body)

        try:
            if not User.objects.filter(email = data['email']).exists():
                return JsonResponse ({"message": "INVALID_USER"}, status=401)

            user_check = User.objects.get(email = data['email'])

            if user_check.password == data['password']:
                return JsonResponse({'message': 'SUCCESS'}, status=200)

            if user_check.password != data['password']:
                return JsonResponse({"message": "INVALID_USER"}, status=401)

        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)

            
