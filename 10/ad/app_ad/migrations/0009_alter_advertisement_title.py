# Generated by Django 4.2.4 on 2023-08-29 10:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_ad', '0008_alter_advertisement_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='title',
            field=models.CharField(max_length=128, validators=[django.core.validators.RegexValidator(inverse_match=True, message='Заголовок не может начинаться с ?', regex='^\\?')], verbose_name='заголовок'),
        ),
    ]
