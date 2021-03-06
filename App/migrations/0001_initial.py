# Generated by Django 2.2 on 2021-06-16 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='solicitacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_do_consultor', models.CharField(max_length=255)),
                ('cliente', models.CharField(max_length=255)),
                ('quadra', models.CharField(max_length=255)),
                ('lote', models.CharField(max_length=255)),
                ('data', models.DateField()),
                ('mensagem', models.TextField()),
                ('status', models.CharField(choices=[('Aguardar', 'Aguardar'), ('Respondido', 'Respondido'), ('Concluido', 'Concluido')], max_length=255)),
            ],
        ),
    ]
