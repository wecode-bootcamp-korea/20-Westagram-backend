from django.urls import path

from user.views  import LogInView, SignUpView, TokenCheckView

urlpatterns = [
    path('/login', LogInView.as_view()),
    path('/signup', SignUpView.as_view()),
    path('/token', TokenCheckView.as_view()),
]
