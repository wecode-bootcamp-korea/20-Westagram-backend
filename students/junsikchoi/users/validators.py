from django.core.exceptions import ValidationError


def validate_email(email):
    required_character = ["@", "."]

    for chracter in required_character:
        if chracter not in email:
            raise ValidationError(
                f"{email} is not an valid email.",
                params={"value": email},
            )


def validate_password(password):
    min_password_length = 8

    if len(str(password)) < min_password_length:
        raise ValidationError(
            "Your Password is too short. Use Longer Password."
        )
