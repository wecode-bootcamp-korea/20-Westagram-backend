import json
from json.decoder     import JSONDecodeError

from django.http      import JsonResponse
from django.views     import View

from user.models      import User
from user.validations import Validation
from user             import errors

class UserView(View):
    def post(self, request):
        # 이메일이나 패스워드 키가 전달되지 않았을 시 에러
        try:
            data = json.loads(request.body)
            email = data['email']
            password = data['password']
        except KeyError:
            return JsonResponse({'message': 'Cannot find required email or password'}, status=400)
        except JSONDecodeError:
            return JsonResponse({'message': 'No input data'}, status=400)

        # 모르는 키가 들어왔을 때 에러
        for keyword in data:
            if keyword not in ('email', 'password', 'phone', 'nickname'):
                return JsonResponse({'message': 'Unknown keyword in request'}, status=400)
         
        # 전화번호, 닉네임이 있다면 저장하고 없다면 None 값 저장
        phone = self.save_keyword('phone', data)
        nickname = self.save_keyword('nickname', data)
        
        # 3 Validations: email, password, duplication
        try:
            Validation.validate_email(self, email)
            Validation.validate_password(self, password)
            Validation.validate_duplication(self, email, phone, nickname)
        except errors.EmailFormatError as e:
            return JsonResponse({'message': e.error_message}, status=400)
        except errors.PasswordError as e:
            return JsonResponse({'message': e.error_message}, status=400)
        except errors.DuplicationError as e:
            return JsonResponse({'message': e.error_message+e.whaterror}, status=400)
        
        # Input data to database
        User.objects.create(email=email, password=password, phone=phone, nickname=nickname)
        
        # Show SUCCESS message
        return JsonResponse({'message': 'SUCCESS'}, status=201)    

    def save_keyword(self, keyword, data):
        try:
            if data[keyword]: 
                return data[keyword] 
            return None  # input이 ''이면 None이 되도록 한다.
        except KeyError: 
            return None  # 입력값이 없어도 None이 되도록 한다. 

class LoginView(View):
    def post(self, request):
        return JsonResponse({'message': 'OK'}, status=200)

