# Generated by Django 3.2.9 on 2021-12-03 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0002_auto_20211203_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='avaliacao',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='curso',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
    ]