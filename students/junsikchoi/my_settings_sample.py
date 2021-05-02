# SAMPLE, change filename to my_settings.py after put in your info.

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "WESTAGRAM",
        "USER": "<YOUR MySQL USERNAME>",
        "PASSWORD": "<YOUR MySQL PWD",
        "HOST": "localhost",
        "PORT": 3306,
    }
}

SECRET_KEY = "<Your Secret Key>"
