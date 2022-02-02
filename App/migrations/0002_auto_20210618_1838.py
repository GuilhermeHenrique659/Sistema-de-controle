# Generated by Django 2.2 on 2021-06-18 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitacao',
            name='respota',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='solicitacao',
            name='status',
            field=models.CharField(choices=[('Aguardar', 'Aguardar'), ('Respondido', 'Respondido'), ('Concluido', 'Concluido')], default='Aguardar', max_length=255),
        ),
    ]
