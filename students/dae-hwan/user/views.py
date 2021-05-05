import json
import re
import bcrypt
import jwt

from django.http   import JsonResponse, HttpResponse
from django.views  import View

from my_settings   import SECRET, ALGORITHM
from user.models   import User

class LogInView(View):
    def post(self, request):
        try:
            data     = json.loads(request.body)
            email    = data['email']
            password = data['password']

            if User.objects.filter(email = email).exists():
                user = User.objects.get(email = email)

                if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                    token = jwt.encode({'user_id': user.id}, SECRET, ALGORITHM)

                    return JsonResponse({'token': token}, status = 200)

            return JsonResponse({'message': 'invalid user'}, status = 401)

        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status = 400)

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
            
            byted_password  = password.encode('utf-8')
            hashed_password = bcrypt.hashpw(byted_password, bcrypt.gensalt())
            db_password     = hashed_password.decode('utf-8')

        
            if nick_name != '' and User.objects.filter(nick_name = nick_name).exists():
                return JsonResponse({'message': 'existing nick_name'}, status = 400)

            if phone_number != '' and User.objects.filter(phone_number = phone_number).exists():
                return JsonResponse({'message': 'existing phone_number'}, status = 400)

            if User.objects.filter(email = email).exists():
                return JsonResponse({'message': 'existing email'}, status = 400)
            
            User.objects.create(
                    email        = email,
                    password     = db_password,
                    nick_name    = data.get('nick_name'),
                    phone_number = data.get('phone_number'),
            )
            return JsonResponse({'message': 'SUCCESS'}, status = 201)

        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status = 400)

class TokenCheckView(View):
    def post(self, request):
        data  = json.loads(request.body)
        token = data['token']

        user_token_info = jwt.decode(token.encode('utf-8'), SECRET, ALGORITHM)

        if User.objects.filter(id = user_token_info['user_id']).exists():
            return HttpResponse(status = 200)
        
        return HttpResponse(status = 403)

