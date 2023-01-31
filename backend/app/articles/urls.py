from django.urls import path

from .views import ArticleViewSet

urlpatterns = [
    path("", ArticleViewSet.as_view({"get": "index"})),
    path("api/articles", ArticleViewSet.as_view({"get": "list"})),
]
