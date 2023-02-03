# System
from django.http import HttpRequest
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

# Project
from config.exception import ApiException
from config.response import create_response
from app.comments.swagger import CommentSwagger
from app.comments.serializers import CommentListSerializer


class CommentViewSet(ViewSet):
    @CommentSwagger.list.swagger
    def list(self, request: HttpRequest, article_id: int) -> Response:
        serializer = CommentListSerializer()

        data = serializer.handle(article_id)
        return create_response(data=data)
