# Generated by Django 3.2 on 2021-07-11 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0046_auto_20210705_1204'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicalcenter',
            name='num_phone_see',
            field=models.IntegerField(default=0, verbose_name='Сколько раз посмотрели номер'),
        ),
    ]
