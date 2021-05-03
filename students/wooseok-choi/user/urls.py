from django.urls import path
from user.views import loginView, signupView

urlpatterns = [
    path('/signup', signupView.as_view()),
    path('/login', loginView.as_view())
]
