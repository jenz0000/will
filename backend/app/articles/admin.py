# System
from django.contrib import admin

# Project
from app.articles.models import Article

admin.site.register(Article)
