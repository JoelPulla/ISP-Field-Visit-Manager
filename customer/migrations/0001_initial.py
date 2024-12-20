# Generated by Django 5.1.3 on 2024-11-08 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ci', models.CharField(max_length=13, verbose_name='Cedula o Ruc')),
                ('name', models.CharField(max_length=50, verbose_name='nombre')),
                ('last_name', models.CharField(max_length=50, verbose_name='Apellido')),
                ('address', models.CharField(max_length=50, verbose_name='Dirección')),
                ('number', models.CharField(max_length=10, verbose_name='Número')),
                ('mail', models.EmailField(max_length=254, null=True, verbose_name='Correo electronico')),
            ],
        ),
    ]
