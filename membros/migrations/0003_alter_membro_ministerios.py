# Generated by Django 3.2 on 2021-05-06 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membros', '0002_auto_20210506_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membro',
            name='ministerios',
            field=models.ManyToManyField(blank=True, to='membros.Ministerio'),
        ),
    ]
