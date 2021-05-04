import json

from django.http            import JsonResponse
from django.views           import View
from django.core.exceptions import ValidationError
from user.models            import User
from user.validators        import validate_email

class SignupView(View):
    def post(self, request):
        data    = json.loads(request.body)
        try:
            if not validate_email(data['email']):
                return JsonResponse({'MASSAGE':'INVALID EMAIL'}, status=400)    
            
            if not len(data['password']) >= 8:
                return JsonResponse({'MASSAGE':'INVALID PASSWORD'}, status=400)

            if not User.objects.filter(email = data['email']):
                return JsonResponse({'MASSAGE':'DUPLICATED EMAIL'}, status=400)

            signup_users = User.objects.create(
                password     = data['password'],
                email        = data['email'],
                name         = data['name'],
                nick_name    = data['nick_name'],
                phone_number = data['phone_number']
            )

            return JsonResponse({'MASSAGE':'SUCCESS'}, status=201)    
        
        except KeyError:
            return JsonResponse({"MASSAGE": "KEY_ERROR"}, status=400)

       