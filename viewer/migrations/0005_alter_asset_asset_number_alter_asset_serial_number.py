# Generated by Django 5.0 on 2024-02-09 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0004_asset_asset_number_asset_serial_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='asset_number',
            field=models.IntegerField(default=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='serial_number',
            field=models.CharField(default=True, max_length=128),
        ),
    ]
