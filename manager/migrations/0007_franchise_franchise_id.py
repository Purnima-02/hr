# Generated by Django 5.0.7 on 2024-10-24 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0006_franchise'),
    ]

    operations = [
        migrations.AddField(
            model_name='franchise',
            name='franchise_id',
            field=models.CharField(blank=True, max_length=1000, null=True, unique=True),
        ),
    ]