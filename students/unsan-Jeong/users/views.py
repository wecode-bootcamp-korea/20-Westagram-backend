import json ,re

from django.http     import JsonResponse, HttpResponse
from django.views    import View

#from django.core.exceptions import ValidationError

from users.models import Users

class SignUp(View):
    def post(self, request):
        data           = json.loads(request.body)
        passwod_length = 8
        try:
            if len(data['password']) < passwod_length:
                return JsonResponse({'MESSAGE':'password of at least eight characters'}, status=404)
            
            if (re.match('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', data['email']) is None):
                return JsonResponse({'MESSAGE':'Invalid email'}, status=400)
            
            if Users.objects.filter(name=data['name']).exists():
                return JsonResponse({'MESSAGE':'Name already exists'}, status=400)
            
            if Users.objects.filter(phone_number=data['phone_number']).exists():
                return JsonResponse({'MESSAGE':'Phone_number already exists'}, status=400)
            
            if Users.objects.filter(email=data['email']).exists():
                return JsonResponse({'MESSAGE':'email already exists'}, status=400)
            
            Users.objects.create(
                name        = data['name'],
                phone_number= data['phone_number'],
                nickname    = data['nickname'],
                age         = data['age'],
                password    = data['password'],
                email       = data['email'],
                )
            return JsonResponse({'MESSAGE':'SUCCESS'}, status=201)
        except KeyError:
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=400)

class LogIn(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            if not Users.objects.fliter(email=data['email']).exists():
                return JsonResponse({"message": "INVALID_USER"}, status=401)
        
            if not Users.objects.fliter(password=data['password']).exists():
                return JsonResponse({"message": "INVALID_USER"}, status=401)
            
            return JsonResponse({'MESSAGE':'SUCCESS'}, status=201)
        except KeyError:
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=400)


    def get(self, request):
        users = Users.objects.all()
        result = []
        for user in users:
            result.append(
                {
                    'user_email': user.email,
                    'name'      : user.name,
                }
            )
        return JsonResponse({'users_results':result}, status=200)