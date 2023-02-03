# System
from django.http import HttpRequest
from rest_framework import serializers

# Project
from config.constants import CODE
from config.exception import ApiException
from config.response import get_ip, get_user_agent
from app.comments.models import Comment
from app.articles.models import Article
from app.articles.serializers import ArticleSerializer


class Commentserializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = ["updated_at", "is_viewable", "article"]


class CommentListSerializer(serializers.Serializer):
    def handle(self, article_id) -> list:
        article = Article.objects.filter(pk=article_id).first()
        if not article:
            raise ApiException(code=CODE.ARTICLE_NOT_FOUND)

        article = ArticleSerializer(article).data

        comments = Comment.objects.filter(article_id=article_id, is_viewable=True)
        comments = Commentserializer(comments, many=True).data

        return {
            "article": article,
            "comments": comments,
        }
