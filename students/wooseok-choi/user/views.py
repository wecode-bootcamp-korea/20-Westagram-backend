import json

from django.http import JsonResponse
from django.views import View

from user.models import User

class UserView(View):
    def post(self, request):
        data = json.loads(request.body)
        
        try:
            data['email']
            data['password']
        except:
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=400) 
        if '@' not in data['email'] or '.' not in data['email']:
            return JsonResponse({'MESSAGE':'INVALID EMAIL'}, status=400)
        elif len(data['password']) < 8:
            return JsonResponse({'MESSAGE':'INVALID PASSWORD'}, status=400)

        User.objects.create(
                user_email = data['email'], 
                user_password = data['password'],
                phone_number = data['phone_number'],
                nickname = data['nickname']
                )
        return JsonResponse({'MESSAGE': 'SUCCESS'}, status=201)
