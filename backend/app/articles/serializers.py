# System
from django.http import HttpRequest
from rest_framework import serializers

# Project
from config.exception import ApiException
from config.response import get_ip, get_user_agent
from app.articles.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        exclude = ["updated_at", "is_viewable"]


class ArticleListSerializer(serializers.Serializer):
    def handle(self) -> list:
        article = Article.objects.filter(is_viewable=True)

        return ArticleSerializer(article, many=True).data


class ArticleCreateSerializer(serializers.Serializer):
    title = serializers.CharField()
    content = serializers.CharField()

    def generate_user_id(self, request: HttpRequest()) -> int:
        ipaddr = get_ip(request)
        user_agent = get_user_agent(request)

        return hash(ipaddr + user_agent)

    def generate_nickname(self, user_id: int) -> str:
        # TODO
        return "부끄러운 당나귀"

    def post_article(
        self,
        user_id: int,
        title: str,
        content: str,
        nickname: str,
        request: HttpRequest,
    ) -> Article:
        return Article.objects.create(
            user_id=user_id,
            title=title,
            content=content,
            nickname=nickname,
        )

    def handle(self, request) -> dict:
        data = self.data

        title = data.get("title")
        content = data.get("content")

        user_id = self.generate_user_id(request)
        nickname = self.generate_nickname(user_id)

        article = self.post_article(user_id, title, content, nickname, request)
        serialized_article = ArticleSerializer(article).data

        return {"article": serialized_article}
