# Generated by Django 3.2.18 on 2023-07-30 04:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('regproductapp', '0004_rename_productview_regproduct'),
    ]

    operations = [
        migrations.RenameField(
            model_name='regproduct',
            old_name='pname',
            new_name='ppname',
        ),
    ]
