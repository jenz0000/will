# System
from django.contrib import admin

# Project
from app.comments.models import Comment

admin.site.register(Comment)
