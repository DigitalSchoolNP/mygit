# Generated by Django 3.0.3 on 2020-05-14 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_auto_20200514_1413'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='featured',
        ),
        migrations.AddField(
            model_name='video',
            name='free',
            field=models.BooleanField(default=False),
        ),
    ]