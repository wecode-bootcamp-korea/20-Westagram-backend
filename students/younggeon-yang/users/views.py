import json

from django.http     import JsonResponse
from django.views    import View

from users.models import User

class UserView(View):
    def post(self, request):
        # 이메일이나 패스워드 키가 전달되지 않았을 시 에러
        try:
            data = json.loads(request.body)
            email = data['email']
            password = data['password']
        except KeyError:
            return JsonResponse({'message': 'Cannot find required email or password'}, status=400)

        # 모르는 키가 들어왔을 때 에러
        for keyword in data:
            if keyword not in ('email', 'password', 'phone', 'nickname'):
                return JsonResponse({'message': 'Unknown keyword in request'}, status=400)
         
        # 전화번호, 닉네임이 있다면 저장하고 없다면 None 값 저장
        phone = self.save_keyword('phone', data)
        nickname = self.save_keyword('nickname', data)
        
        # 3 Validations: email, password, duplication
        try:
            self.validate_email(email)
            self.validate_password(password)
            self.validate_duplication(email, phone, nickname)
        except EmailFormatError as e:
            return JsonResponse({'message': e.error_message}, status=400)
        except PasswordError as e:
            return JsonResponse({'message': e.error_message}, status=400)
        except DuplicationError as e:
            return JsonResponse({'message': e.error_message+e.whaterror}, status=400)
        
        # Input data to database
        User.objects.create(email=email, password=password, phone=phone, nickname=nickname)

        return JsonResponse({'message': 'SUCCESS'}, status=201)    


    def save_keyword(self, keyword, data):
        try:
            if not data[keyword]:  # ""가 입력되면 None이 되도록 한다.
                return None
            return data[keyword]
        except KeyError:  # 입력값이 없어도 None이 되도록 한다.
            return None

    def validate_email(self, mail):
        if '@' not in mail or '.' not in mail:
            raise EmailFormatError
        return

    def validate_password(self, password):
        if len(password) < 8:
            raise PasswordError
        return

    def validate_duplication(self, email, phone, nickname):
        if User.objects.filter(email=email):
            raise DuplicationError("email")
        elif phone and User.objects.filter(phone=phone):  # phone이 None인 경우에는 exception을 피할 수 있다.
            raise DuplicationError("phone")
        elif nickname and User.objects.filter(nickname=nickname):
            raise DuplicationError("nickname")    
        return

    
class EmailFormatError(Exception):
    error_message = "Email format is invalid"
    def __init__(self):
        super().__init__(EmailFormatError.error_message)

class PasswordError(Exception):
    error_message = "Password is too short"
    def __init__(self):
        super().__init__(EmailFormatError.error_message)

class DuplicationError(Exception):
    error_message = "Duplicated user info: "
    def __init__(self, whaterror):
        self.whaterror = whaterror
        super().__init__(EmailFormatError.error_message+whaterror)

