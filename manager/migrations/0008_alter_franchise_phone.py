# Generated by Django 5.0.7 on 2024-10-24 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0007_franchise_franchise_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='franchise',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]