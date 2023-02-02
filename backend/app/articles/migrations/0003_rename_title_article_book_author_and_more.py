# Generated by Django 4.1.5 on 2023-02-02 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("articles", "0002_article_is_viewable"),
    ]

    operations = [
        migrations.RenameField(
            model_name="article",
            old_name="title",
            new_name="book_author",
        ),
        migrations.AddField(
            model_name="article",
            name="book_category",
            field=models.CharField(default="author", max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="article",
            name="book_image_url",
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name="article",
            name="book_title",
            field=models.CharField(default="title", max_length=100),
            preserve_default=False,
        ),
    ]