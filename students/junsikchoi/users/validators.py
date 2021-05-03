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
    MIN_PASSWORD_LENGTH = 8

    if len(str(password)) < MIN_PASSWORD_LENGTH:
        raise ValidationError(
            "Your Password is too short. Use Longer Password."
        )
