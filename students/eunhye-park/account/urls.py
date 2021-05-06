from django.urls import path
from account.views import SignupViews

urlpatterns = [
    path("/signup", SignupViews.as_view()),
]