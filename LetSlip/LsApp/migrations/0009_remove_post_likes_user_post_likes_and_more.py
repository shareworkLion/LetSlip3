# Generated by Django 4.1 on 2022-08-17 14:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('LsApp', '0008_alter_comment_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likes_user',
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterModelTable(
            name='comment',
            table='comment',
        ),
    ]
