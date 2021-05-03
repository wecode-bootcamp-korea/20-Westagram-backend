import re

from user.models import User

def validate_email(email):
    regex = re.compile('^[a-z0-9+-_.]+@[a-z0-9-]+\.[a-z0-9-.]+$', re.I)
    match = regex.match(str(email))
    return bool(match)

def validate_password(password):
    regex = re.compile('^[a-z0-9_-]{8,16}$', re.I)
    match = regex.match(str(password))
    return bool(match)

def duplicate_email(email):
    try:
        User.objects.get(email = email)
        return False
    except:
        return True
