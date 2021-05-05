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
            
            return JsonResponse({'message': 'SUCCESS'}, status=201)
        except KeyError:
            return JsonResponse({'message': 'No keyword'}, status=400)
        except JSONDecodeError:
            return JsonResponse({'message': 'No body'}, status=400)

