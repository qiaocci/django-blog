# Generated by Django 2.0.5 on 2018-05-06 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_comment_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.AddField(
            model_name='comment',
            name='target',
            field=models.CharField(max_length=200, null=True, verbose_name='评论目标'),
        ),
    ]
