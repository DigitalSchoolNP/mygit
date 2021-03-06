# Generated by Django 3.0.3 on 2020-05-16 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memberships', '0003_auto_20200516_1649'),
        ('courses', '0015_course_allowed_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='allowed_user',
        ),
        migrations.AddField(
            model_name='course',
            name='allowed_memberships',
            field=models.ManyToManyField(to='memberships.Membership'),
        ),
    ]
