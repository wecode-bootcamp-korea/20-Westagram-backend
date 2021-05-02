import re

class UserValidation:   # User 모델관련 Validation

    # 필수 입력항목 체크
    def check_required_fields(self, *args):
        return None in args

    # 이메일 형식 체크
    def check_email(self, email):
        email_pattern = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
        return email_pattern.match(email) is None

    # 패스워드 체크
    def check_password(self, password):
        password_pattern = re.compile('^([^ ]{8,}$)+')
        return password_pattern.match(password) is None
