import json
from json.decoder         import JSONDecodeError

from django.http.response import JsonResponse
from django.views         import View
from django.db            import transaction

from .validations         import PostValidation
from .models              import Post, User, Image

class PostView(View):
    def post(self, request):
        post_validation = PostValidation()

        try:
            data       = json.loads(request.body)
            email      = data.get('email')
            content    = data.get('content')
            image_urls = data.get('image_urls')

            if post_validation.check_required_fields(email, content, image_urls):
                return JsonResponse({'message': 'KEY_ERROR'}, status=400)

            if post_validation.check_image_urls(image_urls):
                return JsonResponse({'message': 'IMAGE_URL_ERROR'}, status=400)

            with transaction.atomic():
                user       = User.objects.get(email=email)
                post       = Post.objects.create(user=user, content=content)
                image_list = [Image(post=post, image_url=image_url) for image_url in image_urls]
                Image.objects.bulk_create(image_list)

            return JsonResponse({'message': 'SUCCESS'}, status=201)

        except JSONDecodeError:
            return JsonResponse({'message': 'EMPTY_ARGS_ERROR'}, status=400)

    def get(self, request):
        post_list = Post.objects.all().order_by('-id')
        result    = []

        for post in post_list:
            result.append({
                'post_id'   : post.id,
                'user'      : post.user.email,
                'image_url' : [image.image_url for image in post.image_set.all()],
                'created_at': post.created_at,
            })

        return JsonResponse({'result' : result}, status=200)
