# Generated by Django 3.2 on 2021-06-01 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_medicalcenter_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicalcenter',
            name='this_is',
            field=models.PositiveSmallIntegerField(choices=[(1, 'med center'), (2, 'zoo shop'), (3, 'pharmacy')], default=1),
        ),
    ]