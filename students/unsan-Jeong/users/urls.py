from django.urls import path

from users.views import SingUp

urlpatterns = [
    path('', SingUp.as_view()),
]