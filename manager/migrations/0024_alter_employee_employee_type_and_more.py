# Generated by Django 5.0.7 on 2024-11-06 15:18

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0023_hrcredentials'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='employee_type',
            field=models.CharField(choices=[('Backendemployee', 'Headoffice Employees'), ('customersupport', 'Customer Support'), ('sales', 'sales')], max_length=20),
        ),
        migrations.AlterField(
            model_name='employee',
            name='franchisecode',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
