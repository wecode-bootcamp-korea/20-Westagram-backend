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
                    or Users.objects.filter(nickname = data["nickname"])\
                    or Users.objects.filter(phonenumber = data["phonenumber"]):
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













