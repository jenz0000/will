from django.http import HttpRequest
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response


class ArticleViewSet(ViewSet):
    def index(self, request: HttpRequest) -> Response:
        return Response({"hello": "world"})

    def list(self, request: HttpRequest) -> Response:
        return Response(
            {
                "data": {
                    "articles": [],
                },
                "success": True,
                "code": 0,
            }
        )
