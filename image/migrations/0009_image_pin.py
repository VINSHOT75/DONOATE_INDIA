# Generated by Django 3.1.7 on 2021-04-15 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0008_image_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='pin',
            field=models.CharField(default='', max_length=100),
        ),
    ]
