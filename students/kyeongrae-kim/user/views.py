import json

from django.http import JsonResponse
from django.views import View
from user.models import User
import re

class UsersView(View):
    def post(self, request):
        data = json.loads(request.body)
        users_info = User.objects
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

        try:
            if not (re.search(regex, data['email'])):               #이메일 형식 정규표현식 설정
                raise KeyError                 
            elif len(data['password']) < 8:                         #비밀번호 길이 수 제약
                raise KeyError  
            elif users_info.filter(email=data['email']):            #이메일 중복 방지
                raise ValueError
            elif users_info.filter(username=data['username']):      #유저네임 중복 방지
                raise ValueError
            elif users_info.filter(mobile_num=data['mobile_num']):  #전화번호 중복 방지
                raise ValueError           
            else:                                       
                user = User.objects.create(                         #정상 입력시 회원가입 및 sql에 데이터 저장
                email = data['email'],
                password = data['password'],
                mobile_num = data['mobile_num'],
                username = data['username'],
                )    

        except ValueError:
            return JsonResponse({'중복가입':'ALREADY_EXISTS'}, status=400)
        except KeyError:
            return JsonResponse({'입력오류':'SIGNUP_KEYERROR'}, status=400)

        else:
            return JsonResponse({'회원가입':'SUCCESS'}, status=201)
        



