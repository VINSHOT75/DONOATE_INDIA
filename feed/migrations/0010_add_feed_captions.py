# Generated by Django 3.1.7 on 2021-04-12 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0009_auto_20210413_0100'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_feed',
            name='captions',
            field=models.CharField(default='fuck captions', max_length=100),
        ),
    ]
