from django.urls import path

from .views import ArticleViewSet, ArticleLikeViewSet

urlpatterns = [
    path("api/articles", ArticleViewSet.as_view({"get": "list", "post": "create"})),
    path("api/articles/<int:article_id>/like", ArticleLikeViewSet.as_view({"patch": "partial_update"})),
]
