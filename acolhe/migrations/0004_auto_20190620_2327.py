# Generated by Django 2.2.2 on 2019-06-20 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acolhe', '0003_local_acolhido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='local',
            name='status',
            field=models.CharField(choices=[('OCUPADO', 'ocupado'), ('DISPONIVEL', 'disponível'), ('SOLICITADO', 'solicitado')], default='DISPONIVEL', max_length=20),
        ),
    ]
