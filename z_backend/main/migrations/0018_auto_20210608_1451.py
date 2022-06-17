# Generated by Django 3.2 on 2021-06-08 08:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_alter_bids_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='bids',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bids_customer', to=settings.AUTH_USER_MODEL, verbose_name='Заказчик'),
        ),
        migrations.AlterField(
            model_name='bids',
            name='who',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bids_who', to=settings.AUTH_USER_MODEL, verbose_name='Врач'),
        ),
    ]