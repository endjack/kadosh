# Generated by Django 3.2 on 2021-05-06 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('membros', '0004_auto_20210506_1432'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grupo',
            name='membros',
        ),
        migrations.RemoveField(
            model_name='ministerio',
            name='membros',
        ),
    ]