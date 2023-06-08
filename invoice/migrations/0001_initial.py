# Generated by Django 4.1.7 on 2023-06-06 02:43

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ClientInformation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("client_name", models.CharField(max_length=50, unique=True)),
                ("client_email", models.EmailField(max_length=254, unique=True)),
                ("client_phone_number", models.CharField(max_length=20)),
                ("client_address", models.CharField(max_length=120)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "client information",
                "verbose_name_plural": "clients information",
                "db_table": "ClientInformation",
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="Invoice",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("item", models.CharField(max_length=100)),
                ("quantity", models.IntegerField(default=0)),
                ("amount", models.FloatField(default=0.0)),
                ("total", models.FloatField(default=0.0)),
                ("additional_notes", models.TextField()),
                ("due_date", models.DateTimeField()),
                ("is_paid", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "invoice",
                "verbose_name_plural": "invoices",
                "db_table": "Invoices",
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="PaymentAccount",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("business_name", models.CharField(max_length=50, unique=True)),
                ("business_email", models.EmailField(max_length=254, unique=True)),
                ("business_phone_number", models.CharField(max_length=20)),
                ("bank_name", models.CharField(max_length=50)),
                ("bank_account", models.CharField(max_length=100)),
                ("mobile_payment_name", models.CharField(max_length=50)),
                ("mobile_account", models.CharField(max_length=50)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "payment account",
                "verbose_name_plural": "payment accounts",
                "db_table": "PaymentAccounts",
                "ordering": ["-created_at"],
            },
        ),
    ]
