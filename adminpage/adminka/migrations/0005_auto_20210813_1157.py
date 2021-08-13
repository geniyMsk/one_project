# Generated by Django 3.2.6 on 2021-08-13 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminka', '0004_auto_20210813_1011'),
    ]

    operations = [
        migrations.CreateModel(
            name='phrases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phrase', models.TextField(verbose_name='Фраза')),
            ],
            options={
                'verbose_name': 'фраза',
                'verbose_name_plural': 'фразы',
                'db_table': 'phrases',
            },
        ),
        migrations.AlterModelOptions(
            name='users',
            options={'verbose_name': 'пользователь', 'verbose_name_plural': 'пользователи'},
        ),
        migrations.AlterField(
            model_name='users',
            name='chat_id',
            field=models.BigIntegerField(unique=True, verbose_name='ID пользователя'),
        ),
    ]
