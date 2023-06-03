# Generated by Django 4.1.7 on 2023-06-03 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("reports", "0001_initial"),
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="TransactionCategory",
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
                ("category_name", models.CharField(max_length=100, unique=True)),
                ("category_description", models.TextField()),
            ],
            options={
                "verbose_name": "transaction category",
                "verbose_name_plural": "transaction categories",
                "db_table": "TransactionCategories",
            },
        ),
        migrations.CreateModel(
            name="TransactionType",
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
                (
                    "type_name",
                    models.CharField(
                        choices=[("receivable", "Receivable"), ("payable", "Payable")],
                        max_length=100,
                    ),
                ),
                ("type_description", models.TextField()),
            ],
            options={
                "verbose_name": "transaction type",
                "verbose_name_plural": "transaction types",
                "db_table": "TransactionTypes",
            },
        ),
        migrations.CreateModel(
            name="TransactionSubCategory",
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
                ("category_name", models.CharField(max_length=100, unique=True)),
                ("category_description", models.TextField()),
                (
                    "parent",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="transactions.transactioncategory",
                    ),
                ),
            ],
            options={
                "verbose_name": "transaction sub category",
                "verbose_name_plural": "transaction sub categories",
                "db_table": "TransactionSubCategories",
            },
        ),
        migrations.CreateModel(
            name="TransactionGroup",
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
                ("group_name", models.CharField(max_length=100, unique=True)),
                (
                    "activity",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="reports.businessactivity",
                    ),
                ),
            ],
            options={
                "verbose_name": "transaction group",
                "verbose_name_plural": "transaction groups",
                "db_table": "TransactionGroups",
            },
        ),
        migrations.AddField(
            model_name="transactioncategory",
            name="parent",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="transactions.transactiongroup",
            ),
        ),
        migrations.CreateModel(
            name="Transaction",
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
                ("transaction_amount", models.FloatField(default=0.0)),
                ("currency_code", models.CharField(max_length=3)),
                ("description", models.TextField()),
                ("transaction_date", models.DateTimeField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accounts.account",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="transactions.transactioncategory",
                    ),
                ),
                (
                    "sub_category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="transactions.transactionsubcategory",
                    ),
                ),
                (
                    "transaction_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="transactions.transactiontype",
                    ),
                ),
            ],
            options={
                "verbose_name": "transaction",
                "verbose_name_plural": "transactions",
                "db_table": "Transactions",
                "ordering": ["-created_at"],
            },
        ),
    ]
