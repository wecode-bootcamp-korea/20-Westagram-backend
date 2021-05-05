import json

from django.http     import JsonResponse
from django.views    import View

from user.utils      import login_required
from postings.models import Posting
from user.models     import User

class PostingView(View):
    #@login_required
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

    def get(self, request):
        results = []
        posts = Posting.objects.all()
        for post in posts:
            posting_information = {
                    'email'    : post.user.email,
                    'nick_name': post.user.nick_name,
                    'content'  : post.content,
                    'image_url': post.image_url,
                    'create_at': post.create_at,
                    'update_at': post.update_at,
                }
            results.append(posting_information)
        return JsonResponse({'results': results}, status = 200)
