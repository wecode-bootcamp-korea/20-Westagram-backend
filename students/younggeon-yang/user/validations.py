import re

from user        import errors
from user.models import User

class Validation:
    def validate_email(self, mail):
        regex = re.compile('[a-zA-Z0-9\.\_\+\-]+\@[a-zA-Z0-9\-]+\.[a-zA-Z0-9\.]+')
        if not regex.match(mail):
            raise errors.EmailFormatError
        return

    def validate_password(self, password):
        regex = re.compile('[A-Za-z0-9]{8,}')
        if not regex.match(password):
            raise errors.PasswordError
        return

    def validate_duplication(self, email, phone, nickname):
        if User.objects.filter(email=email):
            raise errors.DuplicationError("email")
        elif phone and User.objects.filter(phone=phone):  # phone이 None인 경우에는 exception을 피할 수 있다.
            raise errors.DuplicationError("phone")
        elif nickname and User.objects.filter(nickname=nickname):
            raise errors.DuplicationError("nickname")
        return

