# Project
from app.articles.models import Article
from rest_framework import serializers


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        exclude = ["updated_at", "is_viewable"]


class ArticleListSerializer(serializers.Serializer):
    def handle(self) -> list:
        article = Article.objects.filter(is_viewable=True)

        return ArticleSerializer(article, many=True).data
