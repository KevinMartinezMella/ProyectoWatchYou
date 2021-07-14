# Generated by Django 2.2.4 on 2021-07-13 23:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('servidores', '0002_remove_servidor_estado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=255)),
                ('fecha_hora', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('servidor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='estado', to='servidores.Servidor')),
            ],
        ),
    ]
