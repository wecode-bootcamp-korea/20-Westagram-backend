import re

from django.core.exceptions   import ValidationError
from django.utils.translation import gettext_lazy as _
from user.models              import SignUp

def validate_email(email):
    email_reg = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    com_reg = re.compile(email_reg)
    mat_reg = com_reg.match(email)
    if mat_reg:
        return True
    else:
        return False
        
def validate_password(password):
    if len(password) >= 8:
        return True
    else:
        return False

def duplicated_email(email):
    if SignUp.objects.filter(email = email):
        return False
    else:
        return True

         



