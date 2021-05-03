from django.urls import path
from user.views import loginView

urlpatterns = [
    path('/login', loginView.as_view()),
]
