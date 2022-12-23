# Generated by Django 3.2.16 on 2022-12-19 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0001_initial'),
        ('registro_hora_extra', '0002_registrohoraextra_horas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrohoraextra',
            name='funcionario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='horas_extra', to='funcionarios.funcionario'),
        ),
    ]
