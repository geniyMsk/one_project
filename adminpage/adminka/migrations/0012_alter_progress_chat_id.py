# Generated by Django 3.2.6 on 2021-08-13 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminka', '0011_auto_20210813_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='progress',
            name='chat_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminka.users'),
        ),
    ]