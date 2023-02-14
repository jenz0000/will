# System
from django.http import HttpRequest
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

# Project
from config.constants import CODE
from config.exception import ApiException
from config.response import create_response
from app.comments.swagger import CommentSwagger, CommentLikeSwagger
from app.comments.serializers import (
    CommentListSerializer,
    CommentCreateSerializer,
    CommentLikePartialUpdateSerializer,
)


class CommentViewSet(ViewSet):
    swagger_tags = ["comments"]

    @CommentSwagger.list.swagger
    def list(self, request: HttpRequest, article_id: int) -> Response:
        serializer = CommentListSerializer()

        data = serializer.handle(article_id)
        return create_response(data=data)

    @CommentSwagger.create.swagger
    def create(self, request: HttpRequest) -> Response:
        serializer = CommentCreateSerializer(data=request.data)

        if not serializer.is_valid():
            raise ApiException(code=CODE.INVALID_PARAMETERS)

        data = serializer.handle()
        return create_response(data=data, status=status.HTTP_201_CREATED)


class CommentLikeViewSet(ViewSet):
    swagger_tags = ["comments"]

    @CommentLikeSwagger.partial_update.swagger
    def partial_update(self, request: HttpRequest, comment_id: int) -> Response:
        serializer = CommentLikePartialUpdateSerializer(data=request.data)

        if not serializer.is_valid():
            raise ApiException()

        data = serializer.handle(request, comment_id)
        return create_response(data=data, status=status.HTTP_200_OK)
