# Generated by Django 3.2 on 2021-06-26 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0035_alter_services_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='PartnerBid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата заявки')),
                ('phone', models.CharField(default='7776665544', max_length=11, verbose_name='Номер без (+7)')),
                ('email', models.CharField(max_length=50, verbose_name='Почта')),
            ],
        ),
    ]