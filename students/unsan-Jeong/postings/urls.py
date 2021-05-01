from django.urls import path, include

from postings.views import PostingsView

urlpatterns = [
    path('', PostingsView.as_view()),
]