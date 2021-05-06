import json

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
                and data.get('phone_number') != none:
                return JsonResponse({'MESSAGE': 'ALREADY_EXISTS'}, status = 400)

            if User.objects.filter(nickname=data.get('nickname')).exists()\
                and data.get('nickname') != none:
                return JsonResponse({'MESSAGE' : 'ALREADY_EXISTS'}, status = 400)

            if User.objects.filter(email=data['email']).exists():
                return JsonResponse({"MESSAGE" : 'ALREADY_EXISTS'}, status = 400)

            PASSWORD_LENGTH = 8
            if len(data['password']) < PASSWORD_LENGTH:
                return JsonResponse({'MESSAGE' : 'INVALID_PASSWORD'}, status = 400)
    
            User.objects.create(
                email         = email,
                password      = password,
                nickname      = nickname,
                phone_number  = phone_number
            )
            return JsonResponse({'Message' : 'SUCCESS'}, status = 201)
        except KeyError:
            return JsonResponse({'MESSAGE' : 'KEY_ERROR'}, status = 400)