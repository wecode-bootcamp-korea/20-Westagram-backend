# WESTAGRAM
Clone of Instagram Backend

## WHAT TO LEARN
- Authentication Process Backend Logic 
- Simple Django CRUD

## REQUIREMENTS
- Python 3.8
- Django
- MySQL
  
## HOW TO RUN
Setup python 3.8 environment + installed local SQL

### Setup MySQL DB
```mysql
# in mysql shell,
# CREATE MySQL DB
create database WESTAGRAM character set utf8mb4 collate utf8mb4_general_ci;
```

### Modify my_settings_sample.py
Enter your SQL Username and Password and rename file to my_settings_sample.py
```python
# SAMPLE, change filename to my_settings.py after put in your info.
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "WESTAGRAM",
        "USER": "user",
        "PASSWORD": "123123",
        "HOST": "localhost",
        "PORT": 3306,
    }
}

SECRET = "somesecretkey"
```

### Setup Python Env & Run with Python
```shell
# in project root
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

