# Generated by Django 3.2 on 2021-07-02 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0042_alter_medicalcenter_district'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата заявки')),
                ('phone', models.CharField(default='7776665544', max_length=10, verbose_name='Номер без (+7)')),
                ('email', models.CharField(max_length=50, verbose_name='Почта')),
                ('message', models.TextField(verbose_name='Текст сообщения')),
            ],
        ),
        migrations.AddField(
            model_name='medicalcenter',
            name='all_time',
            field=models.BooleanField(default=False, verbose_name='Круглосуточно'),
        ),
        migrations.AddField(
            model_name='medicalcenter',
            name='phone2',
            field=models.CharField(default='7776665544', max_length=10, verbose_name='Номер без (+7)'),
        ),
        migrations.AddField(
            model_name='medicalcenter',
            name='phone3',
            field=models.CharField(default='7776665544', max_length=10, verbose_name='Номер без (+7)'),
        ),
        migrations.AlterField(
            model_name='medicalcenter',
            name='phone',
            field=models.CharField(default='7776665544', max_length=10, verbose_name='Номер без (+7)'),
        ),
    ]
