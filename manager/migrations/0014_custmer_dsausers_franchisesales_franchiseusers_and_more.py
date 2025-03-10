# Generated by Django 5.0.7 on 2024-10-25 11:58

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0013_employee_franchisecode'),
    ]

    operations = [
        migrations.CreateModel(
            name='custmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('franchise_id', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DSAUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dsa_registerid', models.CharField(max_length=100, null=True)),
                ('dsa_name', models.CharField(default='name', max_length=100, null=True)),
                ('dsa_password', models.CharField(blank=True, max_length=200, null=True)),
                ('franchiseCode', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='franchisesales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registerid', models.CharField(max_length=100)),
                ('franchiseCode', models.CharField(max_length=100, null=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(max_length=10, null=True)),
                ('pan', models.CharField(blank=True, max_length=12, null=True)),
                ('aadhar', models.CharField(max_length=12, null=True)),
                ('qualification', models.CharField(max_length=30, null=True)),
                ('approval_status', models.CharField(default='pending', max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FranchiseUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('franchise_id', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='dsaowner',
        ),
        migrations.DeleteModel(
            name='franchiseower',
        ),
        migrations.RemoveField(
            model_name='dsa',
            name='franchiserefcode',
        ),
        migrations.RemoveField(
            model_name='sales',
            name='Employe',
        ),
        migrations.RemoveField(
            model_name='sales',
            name='aadhar',
        ),
        migrations.RemoveField(
            model_name='sales',
            name='approval_status',
        ),
        migrations.RemoveField(
            model_name='sales',
            name='email',
        ),
        migrations.RemoveField(
            model_name='sales',
            name='name',
        ),
        migrations.RemoveField(
            model_name='sales',
            name='pan',
        ),
        migrations.RemoveField(
            model_name='sales',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='sales',
            name='qualification',
        ),
        migrations.AddField(
            model_name='dsa',
            name='dsa_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dsa',
            name='dsa_registerid',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dsa',
            name='franchiseCode',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='sales',
            name='password',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='franchisecode',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='sales',
            name='registerid',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='franchisesales',
            name='Employe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
