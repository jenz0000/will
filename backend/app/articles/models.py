# System
from django.db import models

# Project
from config.models import BaseModel


class Article(BaseModel):
    user_id = models.IntegerField()
    content = models.CharField(max_length=500)
    nickname = models.CharField(max_length=500)
    like_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)
    is_viewable = models.BooleanField(default=True)

    book_title = models.CharField(max_length=100)
    book_author = models.CharField(max_length=100)
    book_category = models.CharField(max_length=50)
    book_image_url = models.CharField(max_length=120, null=True)

    class Meta:
        db_table = "app_article"
        app_label = "articles"
