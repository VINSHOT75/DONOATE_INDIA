# Generated by Django 3.1.7 on 2021-05-07 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0020_auto_20210507_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='accno',
            field=models.IntegerField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='image',
            name='hogph',
            field=models.IntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='image',
            name='ifsc',
            field=models.IntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='image',
            name='name',
            field=models.IntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='image',
            name='phone',
            field=models.IntegerField(default=''),
        ),
    ]
