from django.urls import path, include

from postings.views import PostingsView, CommentsView

urlpatterns = [
    path('', PostingsView.as_view()),
    path('/comment/<int:postings_id>', CommentsView.as_view()),
]