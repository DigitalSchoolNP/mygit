# Generated by Django 3.0.3 on 2020-05-12 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20200511_0956'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='position',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
