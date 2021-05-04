import json

from django.http            import JsonResponse
from django.views           import View
from django.core.exceptions import ValidationError
from user.models            import SignUp
from user.validators        import validate_email, validate_password, duplicated_email

class SignUpView(View):
    def post(self, request):
        data    = json.loads(request.body)
        try:
            if not validate_email(data['email']):
                return JsonResponse({'MASSAGE':'INVALID EMAIL'}, status=400)    
            if not validate_password(data['password']):
                return JsonResponse({'MASSAGE':'Password must be at least 8 digits'}, status=400)
            if not duplicated_email(data['email']):
                return JsonResponse({'MASSAGE':'DUPLICATED EMAIL'}, status=400)

            signup_user = SignUp.objects.create(
                password     = data['password'],
                email        = data['email'],
                name         = data['name'],
                nick_name    = data['nick_name'],
                phone_number = data['phone_number']
            )

            return JsonResponse({'MASSAGE':'SUCCESS'}, status=201)    
        
        except KeyError:
            return JsonResponse({"MASSAGE": "KEY_ERROR"}, status=400)

       