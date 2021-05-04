import json
from json.decoder     import JSONDecodeError

from django.http      import JsonResponse
from django.views     import View

from user.models      import User
from user.validations import Validation
from user             import errors

class UserView(View):
    def post(self, request):
        try:
            data     = json.loads(request.body)
            email    = data['email']
            password = data['password']

            # 전화번호, 닉네임이 있다면 저장하고 없다면 None 값 저장
            # dictionary의 get 메소드는 찾는 키 값이 없을 때 원하는 값으로 return할 수 있다.
            # phone or nickname이 ""이면 None으로 바꾼다. MySQL 상에 Null로 넣기 위함.
            phone    = data.get('phone', None)  
            nickname = data.get('nickname', None)
            phone    = None if not phone else phone  
            nickname = None if not nickname else nickname

            # 3 Validations: email, password, duplication
            Validation.validate_email(self, email)
            Validation.validate_password(self, password)
            Validation.validate_duplication(self, email, phone, nickname)

            # Input data to database
            User.objects.create(email=email, password=password, phone=phone, nickname=nickname)

        except KeyError:  # 이메일이나 패스워드 키가 전달되지 않았을 시 에러
            return JsonResponse({'message': 'No email or password'}, status=400)
        except JSONDecodeError:  # Input keyword가 아예 없을 때
            return JsonResponse({'message': 'No input data'}, status=400)
        except errors.EmailFormatError as e:
            return JsonResponse({'message': e.error_message}, status=400)
        except errors.PasswordError as e:
            return JsonResponse({'message': e.error_message}, status=400)
        except errors.DuplicationError as e:
            return JsonResponse({'message': e.error_message+e.whaterror}, status=400)
        return JsonResponse({'message': 'SUCCESS'}, status=201)    


class LoginView(View):
    def post(self, request):
        try:
            data     = json.loads(request.body)
            password = data['password']
       
            email    = data.get('email', None)
            phone    = data.get('phone', None)
            nickname = data.get('nickname', None)

            if email:
                password_db = User.objects.filter(email=email)[0].password
            elif phone:
                password_db = User.objects.filter(phone=phone)[0].password
            elif nickname:
                password_db = User.objects.filter(nickname=nickname)[0].password
            else:
                return JsonResponse({'message': 'No input account'}, status=400)

            if password != password_db:
                return JsonResponse({'message': 'Wrong password'}, status=401)

        except JSONDecodeError:
            return JsonResponse({'message': 'No input data'}, status=400)
        except KeyError:
            return JsonResponse({'message': 'No input password'}, status=400)
        except IndexError:
            return JsonResponse({'message': 'Wrong account name'}, status=401)
        return JsonResponse({'message': 'SUCCESS'}, status=200)
