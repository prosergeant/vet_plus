# Generated by Django 3.2 on 2021-06-01 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_medicalcenter_this_is'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]
