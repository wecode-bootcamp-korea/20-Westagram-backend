from django.shortcuts import render

import json

from django.http            import JsonResponse
from django.views           import View
from user.models            import User
from posting.models         import Posting

import re

class PostingsView(View):
    def post(self, request):
        data      = json.loads(request.body)
        posting   = Posting.objects.create(                            
            user_id         = data['user_id'],    
            #여기는 id말고 유저네임이나 이메일로 추가 시키는 방법 고안해내야함
            image_url       = data['image_url'],
        )
        
        return JsonResponse({"MESSAGE":"POSTING_SUCCESS"}, status=200)


class PostingsGetView(View):
    def get(self, request):
        data      = json.loads(request.body)
        users     = User.objects.all()
        postings  = Posting.objects_set.all()
        results   = []

        for posting in postings:
            results.append(
                {
                    "Username"      : 
                    "Posting Time"  : 
                    "Image URL"     : 
                }
            )