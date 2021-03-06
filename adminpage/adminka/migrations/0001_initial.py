# Generated by Django 3.2.6 on 2021-08-12 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_id', models.BigIntegerField(verbose_name='ID пользователя')),
                ('name', models.TextField(verbose_name='Имя пользователя')),
                ('username', models.TextField(verbose_name='Ник пользователя')),
                ('reg_dt', models.DateTimeField(verbose_name='Дата регистрации')),
            ],
        ),
    ]
