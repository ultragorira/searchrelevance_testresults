# Generated by Django 3.1.7 on 2021-06-15 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_auto_20210614_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='results',
            name='account',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
