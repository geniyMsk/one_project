# Generated by Django 3.2.6 on 2021-08-13 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminka', '0012_alter_progress_chat_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='progress',
            name='chat_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminka.users', unique=True),
        ),
    ]
