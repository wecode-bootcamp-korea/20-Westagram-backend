import jwt
import json

from django.http            import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

from my_settings            import SECRET, ALGORITHM
from user.models            import User

def login_required(orginal_func):
    def wrapper(self, request):
        try:
            access_token    = request.hearders.get('Authorization', None)
            payload         = jwt.decode(access_token.encode('utf-8'), SECRET, ALGORITHM)
            user_id         = User.objects.get(id = payload['user_id'])
            #request.user.id = user_id

            if User.objects.filter(id = user_id):
                return original_func(self, request)

        # 권한이 없는 사용자
        except jwt.exceptions.DecodeError:
            return JsonResponse({'message': 'invalid token'}, status = 403)

        # 익명의 사용자
        except User.DoesNotExist:
            return JsonResponse({'message':' invalid user'}, status = 401)

    return wrapper


