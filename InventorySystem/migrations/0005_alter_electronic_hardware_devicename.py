# Generated by Django 5.0.4 on 2024-04-28 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InventorySystem', '0004_electronic_hardware_devicename'),
    ]

    operations = [
        migrations.AlterField(
            model_name='electronic_hardware',
            name='DeviceName',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
    
    
    
    
