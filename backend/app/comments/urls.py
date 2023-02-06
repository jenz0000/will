# System
from django.urls import path

# Project
from .views import CommentViewSet, CommentLikeViewSet

urlpatterns = [
    path("api/comments", CommentViewSet.as_view({"post": "create"})),
    path("api/comments/<int:article_id>", CommentViewSet.as_view({"get": "list"})),
    path("api/comments/<int:comment_id>/like", CommentLikeViewSet.as_view({"patch": "partial_update"})),
]
