# Generated by Django 5.1.2 on 2024-11-24 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atendente', '0006_delete_chamado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resgate',
            name='descarte',
        ),
        migrations.AlterField(
            model_name='resgate',
            name='status',
            field=models.CharField(max_length=100),
        ),
    ]
