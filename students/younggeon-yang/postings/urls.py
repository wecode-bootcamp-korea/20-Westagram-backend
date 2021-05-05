from django.urls import path

from postings.views  import PostView

urlpatterns = [
    path('/', PostView.as_view()),
#    path('/comments', LoginView.as_view()),
]

