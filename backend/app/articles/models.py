# System
from django.db import models

# Project
from config.models import BaseModel


class Article(BaseModel):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)

    class Meta:
        db_table = "will_article"
        app_label = "articles"
