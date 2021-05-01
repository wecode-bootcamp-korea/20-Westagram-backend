import json

from django.http  import JsonResponse
from django.views import View
from django.db    import IntegrityError

from users.models import User


class SignUpView(View):
    
    def post(self, request):
        users = User.objects.all()
        data  = json.loads(request.body)

        if 'password' not in data.keys() or 'email' not in data.keys():
            return JsonResponse({"MESSAGE": "KEY ERROR"}, status=400)

        elif data['email'].count('@') == 0 or data['email'].count('.') == 0:
            return JsonResponse({"MESSAGE": "EMAIL FORM ERROR"}, status=400)

        elif len(data['password']) < 8:
            return JsonResponse({"MESSAGE": "PASSWORD ERROR"}, status=400)

        else:
            try:
                User.objects.create(
                    email    = data.get('email'),
                    password = data.get('password'),
                    nickname = data.get('nickname'),
                    phone    = data.get('phone')
                )
                return JsonResponse({'MESSAGE':'SIGNUP SUCCESS'}, status=201)
            
            except IntegrityError:
                return JsonResponse({"MESSAGE": "ALREADY EXIT ERROR"}, status=400)