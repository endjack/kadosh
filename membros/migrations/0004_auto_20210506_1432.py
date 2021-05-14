# Generated by Django 3.2 on 2021-05-06 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membros', '0003_alter_membro_ministerios'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grupo',
            name='dia',
        ),
        migrations.RemoveField(
            model_name='ministerio',
            name='dia',
        ),
        migrations.AddField(
            model_name='grupo',
            name='dia_semana',
            field=models.CharField(default='dia', max_length=20),
        ),
        migrations.AddField(
            model_name='ministerio',
            name='dia_semana',
            field=models.CharField(default='dia', max_length=20),
        ),
        migrations.AlterField(
            model_name='grupo',
            name='hora',
            field=models.CharField(default='00:00', max_length=5),
        ),
        migrations.AlterField(
            model_name='ministerio',
            name='hora',
            field=models.CharField(default='00:00', max_length=5),
        ),
    ]