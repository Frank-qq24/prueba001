# Generated by Django 4.0.6 on 2022-08-03 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.TextField(max_length=10)),
                ('nombre', models.TextField()),
                ('horas', models.TextField()),
                ('creditos', models.TextField()),
                ('Fecha_registro', models.TextField()),
                ('estado', models.CharField(max_length=1)),
            ],
        ),
    ]
