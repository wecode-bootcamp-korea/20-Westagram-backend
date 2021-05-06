import json
from json.decoder    import JSONDecodeError

from django.http     import JsonResponse
from django.views    import View

from postings.models import Post, Comment
from user.models     import User


class PostView(View):
    def post(self, request):
        try:
            data    = json.loads(request.body)
            img_url = data['img_url']
            text    = data['text']
            user_id = data['user_id']

            Post.objects.create(
                    img_url=img_url,
                    text=text, 
                    user=User.objects.get(id=user_id)
            )

            return JsonResponse({'message': 'SUCCESS'}, status=201)
        except JSONDecodeError:
            return JsonResponse({'message': 'No body'}, status=400)
        except KeyError:
            return JsonResponse({'message': 'No data'}, status=400)

    def get(self, request):
        results = []
        posts   = Post.objects.all()
        for post in posts:
            result                = {}
            result["user"]        = post.user.email
            result["img_url"]     = post.img_url
            result["text"]        = post.text
            result["time_create"] = post.time_create
            results.append(result)
        return JsonResponse({'message': results}, status=200)


class CommentView(View):
    def post(self, request):
        try:
            data    = json.loads(request.body)
            text    = data['text']
            user_id = data['user_id']
            post_id = data['post_id']

            Comment.objects.create(
                    text=text, 
                    user=User.objects.get(id=user_id), 
                    post=Post.objects.get(id=post_id)
            )

        except JSONDecodeError:
            return JsonResponse({'message': 'No body'}, status=400)
        except KeyError:
            return JsonResponse({'message': 'No data'}, status=400)
        return JsonResponse({'message': 'SUCCESS'}, status=201)

    def get(self, request):
        results = []
        comments = Comment.objects.all()
        for comment in comments:
            result = {}
            result['post_id']     = comment.post_id
            result['user_id']     = comment.user_id
            result['text']        = comment.text
            result['time_create'] = comment.time_create
            results.append(result)

        return JsonResponse({'message': results}, status=200)

class CommentDetailView(View):
    def get(self, request, post_id):
        results = []
        
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return JsonResponse({'message': 'No post_id'}, status=400)

        comments = Comment.objects.filter(post_id=post_id)
        for comment in comments:
            result = {}
            result['post_id']     = comment.post_id
            result['user_id']     = comment.user_id
            result['text']        = comment.text
            result['time_create'] = comment.time_create
            results.append(result)

        return JsonResponse({'message': results}, status=200)