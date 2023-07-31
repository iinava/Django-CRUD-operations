# Generated by Django 4.2.3 on 2023-07-24 06:36

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="contactview",
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
                ("fname", models.CharField(max_length=38)),
                ("lname", models.CharField(max_length=38)),
                ("phone", models.CharField(max_length=12)),
            ],
        ),
    ]
