# Generated by Django 3.2.6 on 2021-08-13 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminka', '0022_delete_progress'),
    ]

    operations = [
        migrations.CreateModel(
            name='progress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chatid', models.IntegerField(verbose_name='123')),
            ],
            options={
                'verbose_name': 'достижение',
                'verbose_name_plural': 'достижения',
                'db_table': 'progress',
            },
        ),
    ]
