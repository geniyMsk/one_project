# Generated by Django 3.2.6 on 2021-08-13 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminka', '0006_auto_20210813_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='chat_id',
            field=models.BigIntegerField(verbose_name='ID пользователя'),
        ),
    ]
