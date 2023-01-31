# System
from django.core.management.base import BaseCommand, CommandError

# Project
from app.articles.models import Article


class Command(BaseCommand):
    """
    python3 manage.py bulk_articles
    """

    def handle(self, *args: any, **options: any) -> None:
        Article.objects.create(
            user_id=13,
            title="가족들은 들으라",
            content="강물이 흘러가는구나\n 내 뼈를 강에 부려다오\n면목이 없다\n강물이여 흘러라",
            nickname="수줍은 거북이",
        )
