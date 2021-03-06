# Generated by Django 3.2 on 2021-05-27 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_teacher_num_phone_see'),
    ]

    operations = [
        migrations.AddField(
            model_name='medreview',
            name='moderate',
            field=models.BooleanField(default=False, verbose_name='Опубликован'),
        ),
        migrations.AddField(
            model_name='medreview',
            name='rating',
            field=models.IntegerField(default=0, verbose_name='Оценка'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='medreview',
            name='review',
            field=models.TextField(default=0, verbose_name='Отзыв'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='medreview',
            name='medcenter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medcenter_medreview', to='main.medicalcenter', verbose_name='Вет клиника'),
        ),
    ]
