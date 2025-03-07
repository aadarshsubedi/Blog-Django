# Generated by Django 5.1.6 on 2025-03-06 11:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("desc", models.TextField()),
                (
                    "img",
                    models.ImageField(blank=True, null=True, upload_to="category/"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Blogs",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("desc", models.TextField()),
                ("img", models.ImageField(blank=True, null=True, upload_to="blog/")),
                ("isfeatured", models.BooleanField(default=False)),
                ("isSlider", models.BooleanField(default=False)),
                (
                    "Category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="Blog.category"
                    ),
                ),
            ],
        ),
    ]
