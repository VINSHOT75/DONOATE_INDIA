# Generated by Django 3.1.7 on 2021-05-09 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0025_auto_20210510_0317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='name',
            field=models.CharField(choices=[('1970', '1970'), ('1971', '1971'), ('1972', '1972'), ('1973', '1973'), ('1974', '1974')], default='green', max_length=6),
        ),
    ]
