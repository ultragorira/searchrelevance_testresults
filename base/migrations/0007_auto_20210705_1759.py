# Generated by Django 3.1.7 on 2021-07-05 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_remove_results_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='results',
            name='id',
        ),
        migrations.AddField(
            model_name='results',
            name='id_result',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
