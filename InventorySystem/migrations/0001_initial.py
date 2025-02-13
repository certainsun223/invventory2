# Generated by Django 5.0.3 on 2024-04-22 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Electronic_Hardware',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('HardwareID', models.IntegerField()),
                ('DeviceSerial', models.CharField(max_length=100)),
                ('CPU', models.CharField(max_length=100)),
                ('GPU', models.CharField(max_length=100)),
                ('RAM', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Hardware',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('HardwareID', models.IntegerField()),
                ('DeviceName', models.CharField(max_length=200)),
                ('Quantity', models.IntegerField()),
                ('Audit', models.DateField(max_length=100)),
                ('Location', models.CharField(max_length=200)),
                ('Status', models.CharField(max_length=100)),
                ('Warranty', models.CharField(max_length=100)),
                ('Comments', models.TextField(max_length=1000)),
                ('OnOffSite', models.CharField(max_length=100)),
                ('RefID', models.IntegerField()),
                ('DeviceType', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Hire_Reference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RefID', models.IntegerField()),
                ('Cost', models.FloatField(max_length=20)),
                ('Hire_StartDate', models.DateField(max_length=20)),
                ('Hire_EndDate', models.DateField(max_length=20)),
                ('UserID', models.CharField(max_length=100)),
                ('AdminID', models.CharField(max_length=100)),
                ('HardwareID', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='NonElectronic_Hardware',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('HardwareID', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserID', models.CharField(max_length=100)),
                ('FirstName', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=250)),
                ('Phone', models.IntegerField()),
                ('Role', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User_Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AdminID', models.CharField(max_length=100)),
                ('FirstName', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=250)),
                ('Phone', models.IntegerField()),
                ('Role', models.CharField(max_length=100)),
            ],
        ),
    ]
