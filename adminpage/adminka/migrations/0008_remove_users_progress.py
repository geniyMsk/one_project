# Generated by Django 3.2.6 on 2021-08-13 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminka', '0007_alter_users_chat_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='progress',
        ),
    ]
