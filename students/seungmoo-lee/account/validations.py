import re

class UserValidation:

    def check_required_fields(self, *args):
        return None in args

    def check_email(self, email):
        email_pattern = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
        return email_pattern.match(email) is None

    def check_password(self, password):
        PASSWORD_LENGTH = 8
        password_pattern = re.compile('^([^ ]{%i,}$)+' % PASSWORD_LENGTH)
        return password_pattern.match(password) is None
