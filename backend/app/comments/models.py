# System
from django.db import models

# Project
from config.models import BaseModel


class Comment(BaseModel):
    article = models.ForeignKey("articles.Article", on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    is_viewable = models.BooleanField(default=True)

    class Meta:
        db_table = "app_comment"
        app_label = "comments"
