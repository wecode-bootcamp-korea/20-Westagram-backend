import json ,re

from django.http     import JsonResponse, HttpResponse
from django.views    import View
from django.core.exceptions import ValidationError

from users.models import Users

class UsersView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            if len(data['password']) < 8:
                return JsonResponse({'MESSAGE':'password of at least eight characters'}, status=404)
            if (re.match('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', data['email']) == None):
                return JsonResponse({'MESSAGE':'Invalid email'}, status=404)
            if (Users.objects.filter(name=data['name']) != None) or (Users.objects.filter(phone_number=data['phone_number']) != None) or (Users.objects.filter(email=data['email']) != None):
                return JsonResponse({'MESSAGE':'Duplicated_KEY'}, status=404)
            Users.objects.create(
                name=data['name'],
                phone_number=data['phone_number'],
                nickname=data['nickname'],
                age=data['age'],
                password=data['password'],
                email=data['email'],
                )
        except KeyError:
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=404)
        return JsonResponse({'MESSAGE':'SUCCESS'}, status=201)
        