import re

from django.core.exceptions   import ValidationError
from django.utils.translation import gettext_lazy as _
from user.models              import User

def validate_email(email):
    email_regex    = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    complied_regex = re.compile(email_regex)
    matched_regex  = complied_regex.match(email)
    if matched_regex: 
        return True
    else:
        return False