# Generated by Django 5.1.3 on 2024-11-24 02:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0002_rename_customer_contract_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='plan',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='contract.plan'),
        ),
    ]
