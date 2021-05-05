import json

from django.views   import View
from django.http    import JsonResponse
from account.models import User
class SignupViews(View):
    def post(self, request):
            data = json.loads(request.body)
    try:

            if email == '' or password == '':
                return JsonResponse({'MESSAGE':'KEY_ERROR'}, status = 400)

            if '@' not in data['email'] or '.' not in data['email']:
                return JsonResponse({'MESSAGE' : 'KEY_ERROR'}, status = 400) 

            if User.objects.filter(phone_number=data.get['phone_number']).exist() \
                 and User.objects.filter(nickname=data.get['phone_number']) != None):
                return JsonResponse({'MESSAGE': 'ALREADY_EXISTS'}, status = 400)

            if User.objects.filter(nickname=data.get['nickname']).exist() \
                 and User.objects.filter(nickname=data.get['nickname']) != None):
                return JsonResponse({'MESSAGE' : 'ALREADY_EXISTS'}, status = 400)

            if User.objects.filter(email=data['email']).exist():
                return JsonResponse({"MESSAGE" : 'ALREADY_EXISTS'}, status = 400)

            PASSWORD_LENGTH = 8
            if len(data['password']) < PASSWORD_LENGTH:
                return JsonResponse({'MESSAGE' : 'INVALID PASSWORD'}, status = 400)
    
            Signup.objects.create(
                email         = email,
                password      = password,
                nickname      = nickname,
                phone_number  = phone_number
            )
            return JsonResponse({'Message' : 'SUCCESS'}, status = 201)
   
        except KeyError:
            return JsonResponse({'MESSAGE' : 'KEYERROR'}, status=400)