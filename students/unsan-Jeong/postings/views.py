import json

from django.http     import JsonResponse, HttpResponse
from django.views    import View

from postings.models import Postings
from users.models import Users

class PostingsView(View):
    def post(self, request):
        data = json.loads(request.body)
        users = Users.objects.all()
        for user in users:
            if user.name == data['name']:
                Postings.objects.create(
                    user_name=data['name'],
                    image_url=data['url'],
                    user=user
                )
                return JsonResponse({'MASSAGE':'SUCCESS'}, status = 201)
            return JsonResponse({'MASSAGE':'Non-existent users'}, status=400)
    def get(self, request):
        postings = Postings.objects.values()
        return JsonResponse({'Postings':list(postings)}, status = 200)