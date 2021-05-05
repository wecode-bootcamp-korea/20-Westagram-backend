import json
from json.decoder     import JSONDecodeError

from django.http      import JsonResponse
from django.views     import View

from user.models      import User
from user.validations import Validation

class SignUpView(View):
    def post(self, request):
        try:
            data     = json.loads(request.body)
            email    = data['email']
            password = data['password']

            phone    = data.get('phone', None)  
            nickname = data.get('nickname', None)
            phone    = None if not phone else phone  
            nickname = None if not nickname else nickname

            if not Validation.validate_email(self, email):
                return JsonResponse({'message': 'Error email'}, status=400)
            if not Validation.validate_password(self, password):
                return JsonResponse({'message': 'Error password'}, status=400)
            if not Validation.validate_duplication(self, email, phone, nickname):
                return JsonResponse({'message': 'Already exist'}, status=400)

            User.objects.create(email=email, password=password, phone=phone, nickname=nickname)
<<<<<<< HEAD

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
=======
            
            return JsonResponse({'message': 'SUCCESS'}, status=201)
        except KeyError:
            return JsonResponse({'message': 'No keyword'}, status=400)
        except JSONDecodeError:
            return JsonResponse({'message': 'No body'}, status=400)

>>>>>>> feature/younggeon-signin
