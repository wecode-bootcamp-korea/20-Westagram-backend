import json

from django.http     import JsonResponse, HttpResponse
from django.views    import View

from postings.models import Postings, Comments
from postings.auth import LoginRequired
from users.models import Users

class PostingsView(View):
    @LoginRequired
    def post(self, request):
        data = json.loads(request.body)
        users = Users.objects.all()
        if Users.objects.filter(id=request.user.id).exists():
            Postings.objects.create(
                name      = data['name'],
                user_name = request.user.name,
                image_url = data['url'],
                user      = request.user,
                #request.user.id
                #Cannot assign "4": "Postings.user" must be a "Users" instance
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
        for user in users:
            for posting in postings:
                if (user.name == data['user_name']) and (posting.name == data['posting_name']):
                    Comments.objects.create(
                        content = data['content'],
                        user = user,
                        post = posting,
                    )
                    return JsonResponse({'MASSEGE':"SUCCESS"}, status =201)
                else:
                    return JsonResponse({'MASSEGE':'Fail'}, status =400)
                
    def get(self, request, postings_id):
        comments = Comments.objects.filter(post=postings_id).values()
        return JsonResponse({'Comments':list(comments)}, status = 200)