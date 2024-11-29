# Generated by Django 5.1.3 on 2024-11-28 20:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0005_rename_mgbytes_plan_megabytes_alter_contract_plan'),
        ('order', '0002_alter_order_order_attetions_alter_order_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='contract',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Responsable', to='contract.contract'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[(0, 'Pendiente'), (1, 'En progreso'), (2, 'Completo'), (3, 'Cancelado')], default=0),
        ),
    ]
