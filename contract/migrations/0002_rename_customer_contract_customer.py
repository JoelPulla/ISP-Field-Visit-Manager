# Generated by Django 5.1.3 on 2024-11-11 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contract',
            old_name='Customer',
            new_name='customer',
        ),
    ]
