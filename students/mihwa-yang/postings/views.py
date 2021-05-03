import json

from django.http     import JsonResponse
from django.views    import View

from users.models    import User
from postings.models import Post

class PostView(View): 
    def post(self, request):
        data  = json.loads(request.body)
        
        try:
            Post.objects.create(
                user    = User.objects.get(email=data['user']),
                img_url = data['img_url']
            )
            return JsonResponse({'MESSAGE':'POSTING SUCCESS'}, status=201)

        except KeyError:
            return JsonResponse({"MESSAGE": "KEY ERROR"}, status=400)

        except:
            return JsonResponse({"MESSAGE": "INVALID USER"}, status=401)


