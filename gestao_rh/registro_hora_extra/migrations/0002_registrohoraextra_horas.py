# Generated by Django 3.2.16 on 2022-12-12 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro_hora_extra', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrohoraextra',
            name='horas',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
