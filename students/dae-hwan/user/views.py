import json 

from django.http  import JsonResponse
from django.views import View

from user.models  import User

class SignUpView(View):
    def post(self, request):
        data                = json.loads(request.body)
        email               = data['email']
        password            = data['password']
        nick_name           = data['nick_name']
        phone_number        = data['phone_number']
        email_validation    = '^[a-z0-9,_-.]+@[a-z0-9,_-]+\.[a-z0-9,_-.]+$'
        password_validation = '.{8,}'

        # 정보가 잘 입력되었을 때
        try: 
            # 이메일에 관한 에러
            if '@' not in email or '.' not in email:
                return JsonResponse({'message': 'email_validation'}, status = 400)
            
            # 비밀번호에 관한 에러
            min_password = 8
            if len(password) < min_password:
                return JsonResponse({'message': 'password validation'}, status = 400)
        
            # 닉네임에 관한 에러
            if User.objects.filter(nick_name = nick_name).exists():
                return JsonResponse({'message': 'nick_name exist'}, status = 400)

            # 전화번호에 관한 에러
            if User.objects.filter(phone_number = phone_number).exists():
                return JsonResponse({'message': 'phone_number exist'}, status = 400)

            # email이 중복되지 않을시 데이터 생성
            if User.objects.filter(email = email).exists():
                return JsonResponse({'message': 'email exist'}, status = 400)
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
