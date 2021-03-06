import json

from django.http            import JsonResponse
from django.views           import View
from user.models            import User
import re

class SignUpView(View):
    def post(self, request):
        data     = json.loads(request.body)
        regex    = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        PASSWORD = 8

        try:
            if not (re.search(regex, data['email'])):                   
                return JsonResponse({'MESSAGE':'EMAIL_KEY_ERROR'}, status=400)
            
            if len(data['password']) < PASSWORD:                               
                return JsonResponse({'MESSAGE':'PASSWORD_KEY_ERROR'}, status=400)
            
            if  User.objects.filter(email=data['email']):                  
                return JsonResponse({'MESSAGE':'USER_ALREADY_EXISTS'}, status=400)
            
            if  User.objects.filter(username=data['username']):           
                return JsonResponse({'MESSAGE':'USER_ALREADY_EXISTS'}, status=400)
            
            if  User.objects.filter(mobile_num=data['mobile_num']):       
                return JsonResponse({'MESSAGE':'USER_ALREADY_EXISTS'}, status=400)   
            
            user = User.objects.create(                            
                email           = data['email'],
                password        = data['password'],
                mobile_num      = data['mobile_num'],
                username        = data['username'],
            )
            return JsonResponse({'MESSAGE':'SUCCESS'}, status=201)

        except KeyError:
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=400)