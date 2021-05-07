from django.urls import path

from accounts.views import AccountView
from accounts.views import LoginView


urlpatterns = [
    path('/users', AccountView.as_view()),
    path('/login', LoginView.as_view()),
]
