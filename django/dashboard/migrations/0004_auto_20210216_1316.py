# Generated by Django 3.1.6 on 2021-02-16 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20210216_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='', editable=False, max_length=200, null=True, unique=True),
        ),
    ]
