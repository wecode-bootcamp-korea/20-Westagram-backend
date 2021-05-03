import json

from django.http  import JsonResponse
from django.views import View
from django.db    import IntegrityError

from users.models import User

class SignUpView(View): 
    def post(self, request):
        data  = json.loads(request.body)

        if 'password' not in data.keys() or 'email' not in data.keys():
            return JsonResponse({"MESSAGE": "KEY ERROR"}, status=400)

        if data['email'].count('@') == 0 or data['email'].count('.') == 0:
            return JsonResponse({"MESSAGE": "EMAIL FORM ERROR"}, status=400)
        
        PASSWORD_LENGTH = 8 
        if len(data['password']) < PASSWORD_LENGTH:
            return JsonResponse({"MESSAGE": "PASSWORD ERROR"}, status=400)

        if User.objects.filter(email=data.get('email')).exists() == True \
            or User.objects.filter(nickname=data.get('nickname')).exists() == True \
            or User.objects.filter(phone=data.get('phone')).exists() == True:
            return JsonResponse({"MESSAGE": "ALREADY EXIT ERROR"}, status=400)
            
        else:
            User.objects.create(
                email    = data.get('email'),
                password = data.get('password'),
                nickname = data.get('nickname'),
                phone    = data.get('phone')
            )
            return JsonResponse({'MESSAGE':'SIGNUP SUCCESS'}, status=201)