# Generated by Django 3.2 on 2021-05-06 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('membros', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ministerio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('dia', models.DateField()),
                ('hora', models.CharField(max_length=5)),
                ('lider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lider_ministerio', to='membros.membro')),
                ('membros', models.ManyToManyField(to='membros.Membro')),
            ],
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.DateField()),
                ('hora', models.CharField(max_length=5)),
                ('lider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lider_grupo', to='membros.membro')),
                ('membros', models.ManyToManyField(to='membros.Membro')),
            ],
        ),
        migrations.AddField(
            model_name='membro',
            name='grupo_membro',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='membros.grupo'),
        ),
        migrations.AddField(
            model_name='membro',
            name='ministerios',
            field=models.ManyToManyField(blank=True, null=True, to='membros.Ministerio'),
        ),
    ]