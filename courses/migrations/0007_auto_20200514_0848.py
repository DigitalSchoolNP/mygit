# Generated by Django 3.0.3 on 2020-05-14 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_auto_20200514_0841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='Full_payment',
            field=models.BooleanField(default=False),
        ),
    ]
