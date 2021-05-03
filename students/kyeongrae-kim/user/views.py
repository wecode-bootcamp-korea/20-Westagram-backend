import json

from django.http            import JsonResponse
from django.views           import View
from django.core.exceptions import ValidationError
from user.models            import User
import re

class UserView(View):
    def post(self, request):
        data = json.loads(request.body)
        users_info = User.objects
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

        try:
            if not (re.search(regex, data['email'])):                   
                return JsonResponse({'SIGNUP':'BAD_REQUEST_KEY_ERROR'}, status=400)
            if len(data['password']) < 8:                               
                return JsonResponse({'SIGNUP':'BAD_REQUEST_KEY_ERROR'}, status=400)
            if users_info.filter(email=data['email']):                  
                return JsonResponse({'SIGNUP':'USER_ALREADY_EXISTS'}, status=400)
            if users_info.filter(username=data['username']):           
                return JsonResponse({'SIGNUP':'USER_ALREADY_EXISTS'}, status=400)
            if users_info.filter(mobile_num=data['mobile_num']):       
                return JsonResponse({'SIGNUP':'USER_ALREADY_EXISTS'}, status=400) 
                  
            else:                                   
                user = User.objects.create(                            
                    email           = data['email'],
                    password        = data['password'],
                    mobile_num      = data['mobile_num'],
                    username        = data['username'],
                )
        except KeyError:
            return JsonResponse({'SIGNUP':'BAD_REQUEST_KEY_ERROR'}, status=400)

        else:
            return JsonResponse({'SIGNUP':'SUCCESS'}, status=201)