import json
from json import JSONDecodeError
from django.db import IntegrityError
from django.views import View
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from users.models import User
from users.validators import (
    validate_email,
    validate_password,
)

class SignUpView(View):
    # Limit HTTP methods to POST
    http_method_names = ["post"]

    # Store Model Fields (Required, non-required)
    required_fields = [_.attname for _ in User._meta.get_fields() if _.blank == False and _.attname != 'id']

    non_required_fields = [_.attname for _ in User._meta.get_fields() if _.blank == True and _.attname != 'id']

    def post(self, request):

        # Response with KEY_ERROR if required key is not contained in the post request
        try:
            req = json.loads(request.body)
        except JSONDecodeError as e:
            return JsonResponse({"message": e.msg}, status=400)
        else:
            for required_field in self.required_fields:
                if required_field not in req.keys():
                    return JsonResponse(
                        {"message": "KEY_ERROR"},
                        status=400,
                    )

        # Validate Email and Password
        try:
            validate_email(req["email"])
            validate_password(req["password"])

        except ValidationError as e:
            return JsonResponse({"message": e.message}, status=400)

        # Get provided column names which are contained both in req.body and model fields
        column_names = list(
            set(req.keys()) 
            & 
            set([*self.required_fields,*self.non_required_fields]))

        data = {k: req[k] for k in column_names}

        try:
            user = User.objects.create(**data)
        except IntegrityError as e:
            return JsonResponse(
                {
                    "message": "DUPLICATED_USER_INFO: {}".format(str(e.__cause__)),
                },
                status=409,
            )
        else:
            return JsonResponse(
                {
                    "message": "SUCCESS",
                    "user": user.to_dict(),
                }
            )
