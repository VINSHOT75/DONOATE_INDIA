# Generated by Django 3.1.7 on 2021-04-24 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0018_auto_20210419_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postimg',
            name='caption',
            field=models.CharField(max_length=500),
        ),
    ]
