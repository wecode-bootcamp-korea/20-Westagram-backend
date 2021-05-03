import json

from django.http  import JsonResponse
from django.views import View

from user.models  import Signup

class SignupView(View):

    def post(self,request):
        data    = json.loads(request.body)
        
        try:
            if (Signup.objects.filter(nick_name=data['nick_name']).exists()) or (Signup.objects.filter(email=data['email']).exists()) or (Signup.objects.filter(phone_number = data['phone_number']).exists()):
                return JsonResponse({'MESSAGE':'User_already_exist'}, status=401)
        
            elif ('@' not in data['email']) or ('.' not in data['email']):
                return JsonResponse({'MESSAGE':'Email_Invalid'}, status=401)
            
            elif len(data['password']) < 8 :
                return JsonResponse({'MESSAGE':'Password_Invalid'}, status=401)
            
            else: Signup.objects.create(
                nick_name=data['nick_name'],
                email=data['email'],
                password=data['password'],
                phone_number=data['phone_number']
                )
            return JsonResponse({'MESSAGE':'SUCCESS'}, status=201)
        except KeyError: 
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=400)


