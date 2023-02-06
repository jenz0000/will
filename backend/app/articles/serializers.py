# System
from django.db.models import F
from django.db import transaction
from django.http import HttpRequest
from rest_framework import serializers

# Project
from config.constants import CODE
from config.exception import ApiException
from config.response import get_ip, get_user_agent
from app.articles.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        exclude = ["updated_at", "is_viewable"]

    def to_representation(self, instance):
        data = super().to_representation(instance)

        data["article_id"] = data.pop("id")

        data["book"] = {}
        data["book"]["title"] = data.pop("book_title")
        data["book"]["author"] = data.pop("book_author")
        data["book"]["category"] = data.pop("book_category")
        data["book"]["image_url"] = data.pop("book_image_url")

        return data


class ArticleListSerializer(serializers.Serializer):
    def handle(self) -> list:
        article = Article.objects.filter(is_viewable=True)

        return ArticleSerializer(article, many=True).data


class ArticleCreateSerializer(serializers.Serializer):
    content = serializers.CharField()

    book_title = serializers.CharField()
    book_author = serializers.CharField()
    book_category = serializers.CharField()
    book_image_url = serializers.CharField(required=False)

    def generate_user_id(self, request: HttpRequest()) -> int:
        ipaddr = get_ip(request)
        user_agent = get_user_agent(request)

        return abs(hash(ipaddr + user_agent))

    def generate_nickname(self, user_id: int) -> str:
        # TODO
        return "부끄러운 당나귀"

    def post_article(self, article_payload: dict) -> Article:
        return Article.objects.create(**article_payload)

    def handle(self, request) -> dict:
        data = self.data

        content = data.get("content")

        book_title = data.get("book_title")
        book_author = data.get("book_author")
        book_category = data.get("book_category")
        book_image_url = data.get("book_image_url")
        user_id = self.generate_user_id(request)
        nickname = self.generate_nickname(user_id)

        article_payload = {
            "content": content,
            "user_id": user_id,
            "book_title": book_title,
            "book_author": book_author,
            "book_category": book_category,
            "book_image_url": book_image_url,
        }

        article = self.post_article(article_payload)
        serialized_article = ArticleSerializer(article).data

        return {"article": serialized_article}


class ArticleLikePartialUpdateSerializer(serializers.Serializer):
    def handle(self, request: HttpRequest, article_id: int) -> dict:
        article = Article.objects.filter(pk=article_id).first()
        if not article:
            raise ApiException(code=CODE.ARTICLE_NOT_FOUND)

        article.change(like_count=F("like_count") + 1)

        article.refresh_from_db()

        serialized_article = ArticleSerializer(article).data
        return {"article": serialized_article}
