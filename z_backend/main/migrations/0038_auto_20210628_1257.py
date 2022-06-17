# Generated by Django 3.2 on 2021-06-28 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0037_alter_medicalcenter_this_is'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bids',
            options={'verbose_name': 'Заявка', 'verbose_name_plural': 'Заявки'},
        ),
        migrations.AlterModelOptions(
            name='completedtask',
            options={'verbose_name': 'Выполненая заявка', 'verbose_name_plural': 'Выполненые заявки'},
        ),
        migrations.AlterModelOptions(
            name='medicalcenter',
            options={'verbose_name': 'Центр', 'verbose_name_plural': 'Центры'},
        ),
        migrations.AlterModelOptions(
            name='medreview',
            options={'verbose_name': 'Отзыв клиники', 'verbose_name_plural': 'Отзывы клиник'},
        ),
        migrations.AlterModelOptions(
            name='partnerbid',
            options={'verbose_name': 'Партнерская заявка', 'verbose_name_plural': 'Партнерские заявки'},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'verbose_name': 'Отзыв врача', 'verbose_name_plural': 'Отзывы врачей'},
        ),
        migrations.AlterModelOptions(
            name='services',
            options={'verbose_name': 'Услуга', 'verbose_name_plural': 'Услуги'},
        ),
        migrations.AlterModelOptions(
            name='teacher',
            options={'verbose_name': 'Врач', 'verbose_name_plural': 'Врачи'},
        ),
        migrations.AlterField(
            model_name='medicalcenter',
            name='this_is',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Вет клиника'), (2, 'Зоомагазин'), (3, 'Аптека'), (4, 'Кинолог'), (5, 'Грумеры')], default=1),
        ),
    ]
