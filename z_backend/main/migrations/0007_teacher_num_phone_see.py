# Generated by Django 3.2 on 2021-05-26 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20210526_1414'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='num_phone_see',
            field=models.IntegerField(default=0, verbose_name='Сколько раз посмотрели номер'),
        ),
    ]
