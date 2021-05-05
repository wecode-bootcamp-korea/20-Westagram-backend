from django.urls import path

from postings.views  import PostView, CommentView

urlpatterns = [
    path('/', PostView.as_view()),
    path('/comments', CommentView.as_view()),
]

