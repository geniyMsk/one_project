# Generated by Django 3.2.6 on 2021-08-13 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminka', '0014_alter_progress_chat_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='chat_id',
            field=models.BigIntegerField(verbose_name='ID пользователя', unique=True),
        ),
    ]
