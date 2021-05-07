from django.urls import path
from account.views import SignupViews, SigninViews

urlpatterns = [
    path('/signup', SignupViews.as_view()),
    path('/signin', SigninViews.as_view())
]