# Generated by Django 3.2 on 2021-06-08 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_completedtask_complete'),
    ]

    operations = [
        migrations.AddField(
            model_name='completedtask',
            name='score',
            field=models.IntegerField(default=0, verbose_name='Оценка'),
        ),
    ]