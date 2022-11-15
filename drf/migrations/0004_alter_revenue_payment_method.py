# Generated by Django 4.1.1 on 2022-11-15 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("drf", "0003_revenue_delete_products"),
    ]

    operations = [
        migrations.AlterField(
            model_name="revenue",
            name="payment_method",
            field=models.CharField(
                blank=True,
                choices=[
                    ("MPESA", "MPESA"),
                    ("NHIF", "NHIF"),
                    ("CASH", "CASH"),
                    ("BANK", "BANK"),
                ],
                max_length=50,
                null=True,
            ),
        ),
    ]