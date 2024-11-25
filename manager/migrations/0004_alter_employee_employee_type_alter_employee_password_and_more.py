# Generated by Django 5.0.7 on 2024-10-09 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_alter_employee_options_alter_employee_managers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='employee_type',
            field=models.CharField(choices=[('personal_loan', 'Personal Loan'), ('home_loan', 'Home Loan'), ('car_loan', 'Car Loan'), ('education_loan', 'Education Loan'), ('lap_loan', 'LAP Loan'), ('other_loan', 'Other Loan'), ('business_loan', 'Business Loan'), ('gold_loan', 'Gold Loan'), ('credit_card_loan', 'Credit Card Loan')], max_length=20),
        ),
        migrations.AlterField(
            model_name='employee',
            name='password',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='employee',
            name='username',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]