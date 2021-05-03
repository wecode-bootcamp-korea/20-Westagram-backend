import json
from json.decoder import JSONDecodeError

from django.http.response import JsonResponse
from django.views         import View
from django.db            import IntegrityError
from django.db.models     import Q

from .models                    import User
from .validations               import UserValidation
from exceptions.customException import ValidError

# 회원가입
class SignUpView(View):
    def post(self, request):
        userValidation = UserValidation()

        try:
            data         = json.loads(request.body)
            email        = data.get('email')
            password     = data.get('password')
            phone_number = data.get('phone_number')
            nickname     = data.get('nickname')

            if userValidation.check_required_fields(email, password):
                raise KeyError()
            if userValidation.check_email(email):
                raise ValidError('EMAIL_ERROR')
            if userValidation.check_password(password):
                raise ValidError('PASSWORD_ERROR')

            User.objects.create(
                email=email,
                password=password,
                phone_number=phone_number,
                nickname=nickname
            )

        except JSONDecodeError as e:
            return JsonResponse({'message': 'EMPTY_ARGS_ERROR'}, status=400)
        except KeyError as e:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)
        except ValidError as e:
            return JsonResponse({'message': f'{e}'}, status=400)
        except IntegrityError as e:
            return JsonResponse({'message': 'ALREADY_EXIST_ERROR'}, status=400)
        except Exception as e:
            return JsonResponse({'message': 'UNKNOWN_ERROR'}, status=400)

        return JsonResponse({'message': 'SUCCESS'}, status=201)

# 로그인
class SignInView(View):
    def post(self, request):
        userValidation = UserValidation()

        try:
            data       = json.loads(request.body)
            account_id = data.get('account_id')
            password   = data.get('password')

            if userValidation.check_required_fields(account_id, password):
                raise KeyError()

            user = User.objects.filter((
                Q(email=account_id) |
                Q(phone_number=account_id) |
                Q(nickname=account_id)) &
                Q(password=password))

            if not user.exists():
                raise ValidError('INVALID_USER')

        except JSONDecodeError as e:
            return JsonResponse({'message': 'EMPTY_ARGS_ERROR'}, status=400)
        except KeyError as e:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)
        except ValidError as e:
            return JsonResponse({'message': f'{e}'}, status=401)
        except Exception as e:
            return JsonResponse({'message': 'UNKNOWN_ERROR'}, status=400)

        return JsonResponse({'message': 'SUCCESS'}, status=200)
