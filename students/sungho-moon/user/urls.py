from django.urls    import path

from user.views import SigninView, UserViews



urlpatterns = [
            path('/signin', SigninView.as_view())
            path('/users', UserView.as_view())
]
