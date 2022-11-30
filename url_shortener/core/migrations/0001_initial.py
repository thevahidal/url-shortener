# Generated by Django 4.1.3 on 2022-11-30 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ShortenedURL",
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
                ("url", models.TextField()),
                ("slug", models.CharField(db_index=True, max_length=10)),
            ],
        ),
    ]
