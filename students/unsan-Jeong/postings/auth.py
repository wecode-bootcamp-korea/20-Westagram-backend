import jwt, json

from django.http import JsonResponse

from my_settings import SECRET
from users.models import Users

class LoginRequired:
    def __init__(self, fuc):
        self.fuc = fuc

    def __call__(self, request, *args, **kwargs):
        token = request.headers.get("Authorization", None)
        try:
            if token is not None:
                payload = jwt.decode(token, SECRET, algorithms = 'HS256')
                user = Users.objects.get(id=payload['user_id'])
                request.user = user
                
                return self.fuc(self, request, *args, **kwargs)

            return JsonResponse({'MESSAGE' : 'NO LOGIN'}, status=401)

        except jwt.DecodeError as e:
            return JsonResponse({'MESSAGE' : f'{e}'}, status=401)
        
        except jwt.InvalidSignatureError:
            return JsonResponse({'MESSAGE' : 'InvalidSignatureError'}, status=401)

        except Users.DoesNotExist:
            return JsonResponse({'MESSAGE' : 'INVALID_USER'}, status=401)