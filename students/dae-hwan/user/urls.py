from django.urls import path

from user.views  import LogInView, SignUpView

urlpatterns = [
    path('/login', LogInView.as_view()),
    path('/signup', SignUpView.as_view()),
]
