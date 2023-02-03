# System
from django.urls import path

# Project
from .views import CommentViewSet

urlpatterns = [
    path("api/comments", CommentViewSet.as_view({"post": "create"})),
    path("api/comments/<int:article_id>", CommentViewSet.as_view({"get": "list"})),
]
