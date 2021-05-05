from django.urls    import path

from user.views import SigninView, UserView



urlpatterns = [
            path('/signin', SigninView.as_view()),
            path('/signup', UserView.as_view())
]
