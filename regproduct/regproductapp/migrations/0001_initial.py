# Generated by Django 4.2.3 on 2023-07-29 05:47

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="regview",
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
                ("name", models.CharField(max_length=38)),
                ("username", models.CharField(max_length=38)),
                ("email", models.CharField(max_length=38)),
                ("phone", models.CharField(max_length=38)),
                ("password", models.CharField(max_length=38)),
            ],
        ),
    ]
