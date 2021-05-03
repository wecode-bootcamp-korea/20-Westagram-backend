import json

from django.http   import JsonResponse
from django.views  import View

from user.models   import User

class LogInView(View):
    def post(self, request):
        try:
            data     = json.loads(request.body)
            email    = data['email']
            password = data['password']

            # 이메일이나 비밀번호가 일치하지 않을 때
            if not User.objects.filter(email = email, password = password).exists():
                return JsonResponse({'message': 'invalid user'}, status = 401)

            return JsonResponse({'message': 'SUCCESS'}, status = 200)

        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status = 400)
