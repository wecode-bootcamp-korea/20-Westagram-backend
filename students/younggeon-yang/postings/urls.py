from django.urls import path

from postings.views  import PostView, CommentView, CommentDetailView

urlpatterns = [
    path('/posts', PostView.as_view()),
    path('/comments', CommentView.as_view()),
    path('/comments/<int:post_id>', CommentDetailView.as_view()),
]

