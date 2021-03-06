# Generated by Django 3.2 on 2021-06-18 13:11

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_medicalcenter_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='bids',
            name='in_med_center',
            field=models.BooleanField(default=False, verbose_name='Заявка у клиники?'),
        ),
        migrations.AddField(
            model_name='bids',
            name='med_center',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.medicalcenter', verbose_name='Мед Центер'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='is_med',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='doc_is_med_foreign', to='main.medicalcenter', verbose_name='Мед центр'),
        ),
        migrations.AlterField(
            model_name='bids',
            name='who',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bids_who', to=settings.AUTH_USER_MODEL, verbose_name='Врач'),
        ),
        migrations.AlterField(
            model_name='medicalcenter',
            name='text',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
