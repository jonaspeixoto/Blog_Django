# Generated by Django 4.1.7 on 2023-02-17 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='resumo',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='titulo',
            field=models.CharField(max_length=255),
        ),
    ]
