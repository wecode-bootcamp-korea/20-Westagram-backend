import json

from django.http     import JsonResponse
from django.views    import View

from postings.models import Posting
from user.models     import User

class PostingView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            email = data['email']

            if not User.objects.filter(email = email).exists():
                return JsonResponse({'MESSAGE': 'invalid user'}, status = 401)

            Posting.objects.create(
                user      = User.objects.get(email = email),
                content   = data['content'] ,
                image_url = data['image_url'],
            )
            return JsonResponse({'message': 'SUCCESS'}, status  = 200)

        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status = 400)


