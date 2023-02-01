# System
from django.db import models

# Project
from config.models import BaseModel


class Article(BaseModel):
    user_id = models.IntegerField()
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    nickname = models.CharField(max_length=500)
    like_count = models.IntegerField(default=0)
    comment_couunt = models.IntegerField(default=0)
    is_viewable = models.BooleanField(default=True)

    class Meta:
        db_table = "app_article"
        app_label = "articles"
