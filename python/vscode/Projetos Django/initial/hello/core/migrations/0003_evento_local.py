# Generated by Django 4.2.2 on 2023-06-24 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_evento_usuario_alter_evento_data_evento'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='local',
            field=models.TextField(default='Descrição evento'),
            preserve_default=False,
        ),
    ]
