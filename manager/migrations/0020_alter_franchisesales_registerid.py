# Generated by Django 5.0.7 on 2024-10-30 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0019_remove_dsa_dsa_id_remove_dsa_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='franchisesales',
            name='registerid',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
