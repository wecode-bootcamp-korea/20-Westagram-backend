import json

from django.http  import JsonResponse
from django.views import View

from user.models  import Users

class SignUpView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            PASSWORD_LENGTH = 8

            if "@" not in data["email"] or "." not in data["email"]:
                return JsonResponse({"MESSAGE" : "INVALID_EMAIL"}, status = 400)

            if len(data["password"]) < PASSWORD_LENGTH:
                return JsonResponse({"MESSAGE" : "INVALID_PASSWORD"}, status = 400)

            if Users.objects.filter(email = data["email"]).exists()\
                    or Users.objects.filter(nickname = data["nickname"]).exists()\
                    or Users.objects.filter(phonenumber = data["phonenumber"]).exists():
                return JsonResponse({"MESSAGE" : "ALREADY_EXIT"}, status = 400)

            Users.objects.create(
                email       = data["email"],
                password    = data["password"],
                nickname    = data["nickname"],
                phonenumber = data["phonenumber"]
            )
            return JsonResponse({"MESSAGE" : "SUCCESS"}, status = 201)

        except KeyError:
            return JsonResponse({"MESSAGE" : "KEY_ERROR"}, status = 400)


class SignInView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            if Users.objects.filter(email = data["email"]).exists() == False:
                return JsonResponse({"MESSAGE" : "INVALID_USER"}, status = 401)

            if data["password"] != Users.objects.get(email=data["email"]).password:
                return JsonResponse({"MESSAGE" : "INVALID_USER"}, status = 401)

            return JsonResponse({"MESSAGE" : "SUCCESS"}, status = 200)

        except KeyError:
            return JsonResponse({"MESSAGE" : "KEY_ERROR"}, status = 400)