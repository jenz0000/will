# System
from django.db.models import F
from django.db import transaction
from django.http import HttpRequest
from rest_framework import serializers

# Project
from config.constants import CODE
from config.exception import ApiException
from config.response import get_ip, get_user_agent
from app.comments.models import Comment
from app.articles.models import Article
from app.articles.serializers import ArticleSerializer


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = ["updated_at", "is_viewable", "article"]

    def to_representation(self, instance):
        data = super().to_representation(instance)

        data["comment_id"] = data.pop("id")

        return data


class CommentListSerializer(serializers.Serializer):
    def handle(self, article_id) -> list:
        article = Article.objects.filter(pk=article_id).first()
        if not article:
            raise ApiException(code=CODE.ARTICLE_NOT_FOUND)

        article = ArticleSerializer(article).data

        comments = Comment.objects.filter(article_id=article_id, is_viewable=True)
        comments = CommentSerializer(comments, many=True).data

        return {
            "article": article,
            "comments": comments,
        }


class CommentCreateSerializer(serializers.Serializer):
    article_id = serializers.IntegerField()
    content = serializers.CharField()

    def handle(self) -> dict:
        data = self.data

        article_id = data.get("article_id")
        content = data.get("content")

        article = Article.objects.filter(pk=article_id).first()
        if not article:
            raise ApiException(code=CODE.ARTICLE_NOT_FOUND)

        with transaction.atomic():
            comment = Comment.objects.create(article_id=article_id, content=content)
            article.change(comment_count=F("comment_count") + 1)

        return {"comment": CommentSerializer(comment).data}


class CommentLikePartialUpdateSerializer(serializers.Serializer):
    def handle(self, request: HttpRequest, comment_id: int) -> dict:
        comment = Comment.objects.filter(pk=comment_id).first()
        if not comment:
            raise ApiException(code=CODE.COMMENT_NOT_FOUND)

        comment.change(like_count=F("like_count") + 1)

        comment.refresh_from_db()

        serialized_comment = CommentSerializer(comment).data
        return {"comment": serialized_comment}
