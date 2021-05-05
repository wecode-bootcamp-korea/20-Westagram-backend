from django.urls import path

from postings.views  import PostView

urlpatterns = [
    path('/posts', PostView.as_view()),
#    path('/comments', LoginView.as_view()),
]

