import json 
import re
import bcrypt

from django.http  import JsonResponse
from django.views import View

from user.models  import User

class SignUpView(View):
    def post(self, request):
        try: 
            data                = json.loads(request.body)
            email               = data['email']
            password            = data['password']
            nick_name           = data.get('nick_name')
            phone_number        = data.get('phone_number')
            email_validation    = re.compile( '^[a-z0-9]+@[a-z0-9]+\.[a-z0-9.]+$', re.I)
            MIN_PASSWORD        = 8          
            password_validation = re.compile('.{%d,}' % (MIN_PASSWORD))

            if not email_validation.match(email):
                return JsonResponse({'message': 'invalid email'}, status = 400)
            
            if not password_validation.match(password):
                return JsonResponse({'message': 'invalid password'}, status = 400)
            hashed_password= bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        
            if nick_name != None and User.objects.filter(nick_name = nick_name).exists():
                return JsonResponse({'message': 'existing nick_name'}, status = 400)

            if phone_number != None and User.objects.filter(phone_number = phone_number).exists():
                return JsonResponse({'message': 'existing phone_number'}, status = 400)

            if User.objects.filter(email = email).exists():
                return JsonResponse({'message': 'existing email'}, status = 400)
            
            User.objects.create(
                    email        = email,
                    password     = hashed_password,
                    nick_name    = data.get('nick_name'),
                    phone_number = data.get('phone_number'),
            )
            return JsonResponse({'message': 'SUCCESS'}, status = 201)

        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status = 400)

