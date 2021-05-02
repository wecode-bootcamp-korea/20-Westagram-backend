from django.db import models

class User(models.Model):                                                       # 회원 정보
    email           = models.EmailField(max_length=100, unique=True)            # 이메일
    password        = models.CharField(max_length=200)                          # 패스워드
    phone_number    = models.CharField(max_length=100, unique=True, null=True)  # 핸드폰 번호
    nickname        = models.CharField(max_length=100, unique=True, null=True)  # 닉네임
    created_at      = models.DateTimeField(auto_now_add=True)                   # 가입 날짜
    updated_at      = models.DateTimeField(auto_now=True)                       # 수정 날짜

    class Meta:
        db_table = 'users'