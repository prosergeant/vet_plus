# Generated by Django 3.2 on 2021-06-21 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0030_merge_0027_auto_20210618_1911_0029_teacher_is_med'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicalcenter',
            name='this_is',
            field=models.PositiveSmallIntegerField(choices=[(1, 'med center'), (2, 'zoo shop'), (3, 'pharmacy'), (4, 'service')], default=1),
        ),
    ]