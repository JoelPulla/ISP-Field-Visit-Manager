# Generated by Django 5.1.3 on 2024-11-25 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0003_alter_contract_plan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='address',
            field=models.CharField(max_length=50, verbose_name='Dirección'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='box',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Coordenadas Caja'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='coordinates',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Coordenadas Ubicación'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Status Activo'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='ont',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='SN ONT'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='router',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='SN Router'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='url_gps',
            field=models.URLField(blank=True, null=True, verbose_name='URL GPS'),
        ),
    ]
