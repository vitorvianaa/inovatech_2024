# Generated by Django 5.1.2 on 2024-11-20 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipe_coleta', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chamadocoleta',
            name='status',
            field=models.CharField(choices=[('CRIADA', 'CRIADA'), ('EM ANDAMENTO', 'EM ANDAMENTO'), ('INCOMPLETA', 'INCOMPLETA'), ('SUCESSO', 'SUCESSO'), ('FALHA', 'FALHA'), ('PENDENTE', 'PENDENTE'), ('FECHADO', 'FECHADO')], max_length=100),
        ),
    ]
