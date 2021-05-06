import json

from django.http     import JsonResponse
from django.views    import View

from user.utils      import login_required
from postings.models import Posting, Comment
from user.models     import User

class PostingView(View):
    @login_required
    def post(self, request):
        data = json.loads(request.body)
        try:
            user      = request.user
            content   = data['content']
            image_url = data.get('image_url')

            Posting.objects.create(
                user      = request.user,
                content   = content,
                image_url = image_url,
            )
            return JsonResponse({'message': 'SUCCESS'}, status  = 200)

        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status = 400)

    @login_required
    def get(self, request):
        posting_data = Posting.objects.values()
        return JsonResponse({'posting_list': list(posting_data)}, status = 200)

class CommentView(View):
    def post(self, request):
        try:
            data     = json.loads(request.body)
            content  = data['content']
            email    = data['email']
            comments = data['comments']

            if not User.objects.filter(email = email).exists():
                return JsonResponse({'message': 'invalid user'}, status = 401)

            if not Posting.objects.filter(content = content).exists():
                return JsonResponse({'message': 'invalid posting'}, status = 401)

            Comment.objects.create(
                    posting  = Posting.objects.get(content = content),
                    user     = User.objects.get(email = email),
                    comments = comments,
            )
            return JsonResponse({'message': 'SUCCESS'}, status =200)
        
        except KeyError:
            JsonResponse({'message': 'KEY_ERROR'}, status = 400)
                    
    def get(self, request):
        results = []
        comments = Comment.objects.all()
        for comment in comments:
            comment_information = {
                    'posting cotent': comment.posting.content,
                    'user email'    : comment.user.email,
                    'comments'      : comment.comments,
            }
            results.append(comment_information)
        return JsonResponse({'results': results}, status = 200)
