# Generated by Django 3.2.16 on 2022-12-12 19:51

from django.db import migrations, models
import gestao_rh.documentos.models


class Migration(migrations.Migration):

    dependencies = [
        ('documentos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='documento',
            name='arquivo',
            field=models.FileField(blank=True, null=True, upload_to=gestao_rh.documentos.models.arquivo_documento_directory_path),
        ),
    ]
