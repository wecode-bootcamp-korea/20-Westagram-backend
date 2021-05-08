import json
from json.decoder import JSONDecodeError

from django.http.response import JsonResponse
from django.views         import View
from django.db.models     import Q

from .models              import User
from .validations         import UserValidation

class SignUpView(View):
    def post(self, request):
        user_validation = UserValidation()

        try:
            data         = json.loads(request.body)
            email        = data.get('email')
            password     = data.get('password')
            phone_number = data.get('phone_number')
            nickname     = data.get('nickname')

            if user_validation.check_required_fields(email, password):
                return JsonResponse({'message': 'KEY_ERROR'}, status=400)

            if user_validation.check_email(email):
                return JsonResponse({'message': 'EMAIL_ERROR'}, status=400)

            if user_validation.check_password(password):
                return JsonResponse({'message': 'PASSWORD_ERROR'}, status=400)

            user = User.objects.filter((
                Q(email=email) |
                Q(phone_number=phone_number) |
                Q(nickname=nickname)
            ))

            if user.exists():
                return JsonResponse({'message': 'ALREADY_EXIST_ERROR'}, status=400)

            User.objects.create(
                email=email,
                password=password,
                phone_number=phone_number,
                nickname=nickname
            )

            return JsonResponse({'message': 'SUCCESS'}, status=201)

        except JSONDecodeError:
            return JsonResponse({'message': 'EMPTY_ARGS_ERROR'}, status=400)

class SignInView(View):
    def post(self, request):
        userValidation = UserValidation()

        try:
            data       = json.loads(request.body)
            account_id = data.get('account_id')
            password   = data.get('password')

            if userValidation.check_required_fields(account_id, password):
                return JsonResponse({'message': 'KEY_ERROR'}, status=400)

            user = User.objects.filter((
                Q(email=account_id) |
                Q(phone_number=account_id) |
                Q(nickname=account_id)) &
                Q(password=password))

            if not user.exists():
                return JsonResponse({'message': 'INVALID_USER'}, status=401)

            return JsonResponse({'message': 'SUCCESS'}, status=200)

        except JSONDecodeError:
            return JsonResponse({'message': 'EMPTY_ARGS_ERROR'}, status=400)
