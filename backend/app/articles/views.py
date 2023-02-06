# System
from django.http import HttpRequest
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

# Project
from config.exception import ApiException
from config.response import create_response
from app.articles.swagger import ArticleSwagger
from app.articles.serializers import (
    ArticleListSerializer,
    ArticleCreateSerializer,
    ArticleLikePartialUpdateSerializer,
)


class ArticleViewSet(ViewSet):
    swagger_tags = ["articles"]

    @ArticleSwagger.list.swagger
    def list(self, request: HttpRequest) -> Response:
        serializer = ArticleListSerializer()

        articles = serializer.handle()
        return create_response(data={"articles": articles})

    @ArticleSwagger.create.swagger
    def create(self, request: HttpRequest) -> Response:
        serializer = ArticleCreateSerializer(data=request.data)

        if not serializer.is_valid():
            raise ApiException()

        data = serializer.handle(request)
        return create_response(data=data, status=status.HTTP_201_CREATED)


class ArticleLikeViewSet(ViewSet):
    swagger_tags = ["articles"]

    def partial_update(self, request: HttpRequest, article_id: int) -> Response:
        serializer = ArticleLikePartialUpdateSerializer(data=request.data)

        if not serializer.is_valid():
            raise ApiException()

        data = serializer.handle(request, article_id)
        return create_response(data=data, status=status.HTTP_200_OK)
