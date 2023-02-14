# System
from django.contrib import admin
from django.urls import path, include, re_path

# Project
from config.swagger import schema_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("app.articles.urls")),
    path("", include("app.comments.urls")),
]

urlpatterns += [
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    re_path(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    re_path(
        r"^redoc/$",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
]
