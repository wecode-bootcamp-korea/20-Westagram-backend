from django.urls import path

from user.views import SignupView

urlpatterns = [
    path('', SignupView.as_view())
]