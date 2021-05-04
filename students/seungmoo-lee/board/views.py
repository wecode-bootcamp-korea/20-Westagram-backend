import json
from json.decoder         import JSONDecodeError

from django.http.response import JsonResponse
from django.views         import View

from .validations         import PostValidation
from .models              import Post, User

class PostView(View):
    def post(self, request):
        post_validation = PostValidation()

        try:
            data       = json.loads(request.body)
            email      = data.get('email')
            image_url  = data.get('image_url')

            if post_validation.check_required_fields(email, image_url):
                return JsonResponse({'message': 'KEY_ERROR'}, status=400)

            if post_validation.check_image_url(image_url):
                return JsonResponse({'message': 'IMAGE_URL_ERROR'}, status=400)

            user = User.objects.get(email=email)
            Post.objects.create(user=user, image_url=image_url)

            return JsonResponse({'message': 'SUCCESS'}, status=201)

        except JSONDecodeError:
            return JsonResponse({'message': 'EMPTY_ARGS_ERROR'}, status=400)

    def get(self, request):
        post_list = Post.objects.all().order_by('-id')
        result = []

        for post in post_list:
            result.append({
                'post_id': post.id,
                'user': post.user.email,
                'image_url': post.image_url,
                'created_at': post.created_at,
            })

        return JsonResponse({'result' : result}, status=200)
