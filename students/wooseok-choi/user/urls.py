from django.urls import path
from user.views import loginView, signupView

urlpatterns = [
    path('/login', loginView.as_view()),
    path('/signup', signupView.as_view()),
]
