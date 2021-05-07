from django.urls import path

from accounts.views import AccountView

urlpatterns = [
    path('/signup', AccountView.as_view())
]
