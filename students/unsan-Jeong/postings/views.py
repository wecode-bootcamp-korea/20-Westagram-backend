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

class CommentsView(View):
    def post(self, request):
        data = json.loads(request.body)
        users = Users.objects.all()
        postings = Postings.objects.all()
        comment = Comments.obejcts.create(
            content = data['content']
        )
        for user in users:
            if user.name == data['user']:
                comment.user.add(user.id)
            else:
                return JsonResponse({'MASSEGE':'Non-existent users'}, status =400)
        for posting in postings:
            if posting.name == data['posting']:
                comment.post.add(posting.id)
            else: 
                return JsonResponse({'MASSEGE':'Non-existent posting'}, status =400)
        return JsonResponse({'MASSEGE':"SUCCESS"}, status =2o0)

    def get(self, request):
        comments = Comments.objects.values()
        return JsonResponse({'Comments':list(comments)}, status = 200)