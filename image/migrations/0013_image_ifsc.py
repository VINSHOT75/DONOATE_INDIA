# Generated by Django 3.1.7 on 2021-04-15 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0012_image_hogph'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='ifsc',
            field=models.CharField(default='', max_length=100),
        ),
    ]
