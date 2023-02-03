from django.urls import path

from .views import ArticleViewSet

urlpatterns = [
    path("api/articles", ArticleViewSet.as_view({"get": "list", "post": "create"})),
]
