# Generated by Django 3.1.7 on 2021-06-07 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='results',
            name='email',
            field=models.EmailField(blank=True, max_length=100, unique=True),
        ),
    ]
