import json

from django.http  import JsonResponse
from django.views import View

from user.models import User
from user.validate import validate_email, validate_password

class SignupView(View):
    def post(self, request):
        data = json.loads(request.body)
        
        try:
            if not validate_email(data['email']):
                return JsonResponse({'message':'INVALID EMAIL'}, status=400)

            if not validate_password(data['password']):
                return JsonResponse({'message':'INVALID PASSWORD'}, status=400)
            
            if User.objects.filter(email = data['email']).exists():
                return JsonResponse({'message':'DUPLICATE EMAIL'}, status=409)

            User.objects.create(
                email         = data.get('email'), 
                password      = data.get('password'),
                phone_number  = data.get('phone_number'),
                nickname      = data.get('nickname')
                )
            return JsonResponse({'message': 'SUCCESS'})

        except:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)
