# Generated by Django 5.1.2 on 2024-11-20 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atendente', '0004_pontoscoleta_complemento'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoscoleta',
            name='bairro',
            field=models.CharField(default='none', max_length=100),
        ),
    ]
