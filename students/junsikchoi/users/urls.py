from django.urls import path
from users.views import SignInView, SignUpView

urlpatterns = [
    path(
        "/signUp",
        SignUpView.as_view(),
    ),
    path(
        "/signIn",
        SignInView.as_view(),
    ),
]
