from django.urls import path
from user.views  import LogInView

urlpatterns = [
    path('/login', LogInView.as_view()),
]
