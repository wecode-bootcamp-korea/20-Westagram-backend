import json

from django.http  import JsonResponse
from django.views import View

from user.models  import User

class UserView(View):

    def post(self,request):
        data    = json.loads(request.body)
        PW_MIN_LENGTH = 8

        data_email       = data['email']
        data_password    = data['password']
        data_nickname    = data.get('nickname')
        data_phonenumber = data.get('phonenumber')

        try:
            if (User.objects.filter(email=data_email).exists()):
                return JsonResponse({'MESSAGE':'User_already_exist'}, status=401)

            if ('@' not in data['email']) or ('.' not in data['email']):
                return JsonResponse({'MESSAGE':'Email_Invalid'}, status=401)

            if (data_nickname != None) and (USER.objects.filter(nick_name=data_nickname).exists()): 
                return JsonResponse({'MESSAGE':'User_already_exist'}, status=401)

            if (data_phonenumber != None) and (User.objects.filter(phone_number = data['phone_number']).exists()):
                return JsonResponse({'MESSAGE':'User_already_exist'}, status=401)
            
            if len(data['password']) < PW_MIN_LENGTH :
                return JsonResponse({'MESSAGE':'Password_Invalid'}, status=401)
            
            User.objects.create(
                nick_name   =data_nickname,
                email       =data_email,
                password    =data_password,
                phone_number=data_phonenumber
                )
            return JsonResponse({'MESSAGE':'SUCCESS'}, status=201)
        except KeyError: 
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=400)


class SigninView(View):
    def post(self, request):
        data=json.loads(request.body)
	    
        signin_email    = data['email']
        signin_password = data['password']

        if not signin_email and not signin_password:
        	return JsonResponse({"messege":"KEYERROR"}, status=400)
       
        if not User.objects.filter(email=signin_email).exists() :
        	return JsonResponse({'messege":"INVALID_EMAIL'}, status=400)
       
        if not User.objects.get(email=signin_email).password == signin_password:
            return JsonResponse({"messege":"INVALID_PASSWORD"}, status=400)
	
        return JsonResponse({"messege":"SUCCESS"}, status=200)       
