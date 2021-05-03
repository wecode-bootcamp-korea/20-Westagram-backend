from django.urls import path, include

from postings.views import PostingsView, CommentsView

urlpatterns = [
    path('', PostingsView.as_view()),
    path('/comment', CommentsView.as_view()),
]