from django.urls import path
from user.views import UsersView

urlpatterns = [
    path('user', UsersView.as_view()),
    ]
