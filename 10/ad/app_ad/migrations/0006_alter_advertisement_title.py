# Generated by Django 4.2.4 on 2023-08-29 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_ad', '0005_alter_advertisement_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='title',
            field=models.CharField(max_length=128, verbose_name='заголовок'),
        ),
    ]
