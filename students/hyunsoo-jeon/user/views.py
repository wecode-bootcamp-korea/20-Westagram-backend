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

            elif len(data['password']) < 8:
                 return JsonResponse ({"message": "This password is too short"}, status=400)

            elif User.objects.filter(email = data['email']).exists():
                return JsonResponse ({"message": "This email already exists."}, status=400)

            else:
                User.objects.create(
                        email    = data['email'],
                        password = data['password']
                    )
                return JsonResponse ({"message": "SUCCESS"}, status=200)

        except KeyError:
            return JsonResponse({"message" : 'KEY_ERROR'}, status=400)
