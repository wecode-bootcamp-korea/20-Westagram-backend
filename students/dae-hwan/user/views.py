import json 
import re

from django.http  import JsonResponse
from django.views import View

from user.models  import User

class SignUpView(View):
    def post(self, request):

        # 정보가 잘 입력되었을 때
        try: 
            data                = json.loads(request.body)
            email               = data['email']
            password            = data['password']
            nick_name           = data['nick_name']
            phone_number        = data['phone_number']

            # 이메일은 @와 .을 필수로 포함
            email_validation    = re.compile( '^[a-z0-9]+@[a-z0-9]+\.[a-z0-9.]+$', re.I)

            # 비밀번호의 최소자리수
            MIN_PASSWORD        = 8
            password_validation = re.compile('.{%d,}' % (MIN_PASSWORD))


            # 이메일은 @와 .을 필수로 포함
            email_validation    = re.compile( '^[a-z0-9]+@[a-z0-9]+\.[a-z0-9.]+$', re.I)

            # 비밀번호의 최소자리수
            MIN_PASSWORD        = 8          
            password_validation = re.compile('.{%d,}' % (MIN_PASSWORD))

            # 이메일에 관한 에러
            if not email_validation.match(email):
                return JsonResponse({'message': 'invalid email'}, status = 400)
            
            # 비밀번호에 관한 에러
            if not password_validation.match(password):
                return JsonResponse({'message': 'invalid password'}, status = 400)
        
            # 닉네임에 관한 에러
            if User.objects.filter(nick_name = nick_name).exists():
                return JsonResponse({'message': 'existing nick_name'}, status = 400)

            # 전화번호에 관한 에러
            if User.objects.filter(phone_number = phone_number).exists():
                return JsonResponse({'message': 'existing phone_number'}, status = 400)

            # email이 중복되지 않을시 데이터 생성
            if User.objects.filter(email = email).exists():
                return JsonResponse({'message': 'existing email'}, status = 400)
            
            User.objects.create(
                    email        = email,
                    password     = password,
                    nick_name    = nick_name,
                    phone_number = phone_number,
            )
            return JsonResponse({'message': 'SUCCESS'}, status = 201)

        # 정보를 틀리게 입력했을 때
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status = 400)

