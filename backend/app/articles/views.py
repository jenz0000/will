# System
from django.http import HttpRequest
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

# Project
from config.response import create_response
from app.articles.serializers import ArticleListSerializer


class ArticleViewSet(ViewSet):
    def index(self, request: HttpRequest) -> Response:
        return Response({"hello": "world"})

    def list(self, request: HttpRequest) -> Response:
        serializer = ArticleListSerializer()

        articles = serializer.handle()
        return create_response(data={"articles": articles})
