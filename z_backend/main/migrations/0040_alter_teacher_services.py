# Generated by Django 3.2 on 2021-06-28 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0039_alter_medicalcenter_this_is'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='services',
            field=models.ManyToManyField(blank=True, to='main.Services', verbose_name='К какой услуге относится'),
        ),
    ]