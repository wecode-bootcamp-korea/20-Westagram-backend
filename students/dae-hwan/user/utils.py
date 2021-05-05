import jwt
import json

from django.http            import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

from my_settings            import SECRET
from user.models            import User

def login_required(orginal_func):
    def wrapper(self, request):
        try:
            access_token = request.hearders.get('Authorization', None)

            if access_token:
                payload      = jwt.decode(access_token, SECRET, algorithms = ['HS256'])
                request.user = User.objects.get(id = payload['user_id'])

                return orginal_func(self, request)

            return JsonResponse({'message': 'login required'}, status = 401)
        
        # 권한이 없는 사용자
        except jwt.exceptions.DecodeError:
            return JsonResponse({'message': 'invalid token'}, status = 403)

        # 익명의 사용자
        except User.DoesNotExist:
            return JsonResponse({'message':' invalid user'}, status = 401)

    return wrapper


