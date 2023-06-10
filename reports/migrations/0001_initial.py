# Generated by Django 4.2.2 on 2023-06-10 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CashFlowRecord",
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
                ("uid", models.CharField(max_length=50)),
                ("category", models.CharField(max_length=100)),
                ("item", models.CharField(max_length=100)),
                ("activity", models.CharField(max_length=50)),
                ("amount", models.FloatField(default=0.0)),
                ("is_income", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "cash flow record",
                "verbose_name_plural": "cash flow records",
                "db_table": "CashFlowRecords",
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="IncomeStatement",
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
                ("uid", models.CharField(max_length=50)),
                ("period_start_date", models.DateField()),
                ("period_end_date", models.DateField()),
                ("revenue", models.FloatField(default=0.0)),
                ("gross_profit", models.FloatField(default=0.0)),
                ("operating_expenses", models.FloatField(default=0.0)),
                ("net_income", models.FloatField(default=0.0)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accounts.account",
                    ),
                ),
            ],
            options={
                "verbose_name": "income statement",
                "verbose_name_plural": "income statements",
                "db_table": "IncomeStatements",
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="CashFlowStatementIdentifier",
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
                ("uid", models.CharField(max_length=50)),
                ("period_start_date", models.DateField()),
                ("period_end_date", models.DateField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accounts.account",
                    ),
                ),
            ],
            options={
                "verbose_name": "cash flow statement identifier",
                "verbose_name_plural": "cash flow statements identifiers",
                "db_table": "CashFlowStatementsIdentifiers",
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="CashFlowStatement",
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
                ("uid", models.CharField(max_length=50)),
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
                    "record",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="reports.cashflowrecord",
                    ),
                ),
            ],
            options={
                "verbose_name": "cash flow statement",
                "verbose_name_plural": "cash flow statements",
                "db_table": "CashFlowStatements",
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="BalanceSheetStatement",
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
                ("uid", models.CharField(max_length=50)),
                ("assets", models.FloatField(default=0.0)),
                ("liabilities", models.FloatField(default=0.0)),
                ("equity", models.FloatField(default=0.0)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accounts.account",
                    ),
                ),
            ],
            options={
                "verbose_name": "balance sheet statement",
                "verbose_name_plural": "balance sheet statements",
                "db_table": "BalanceSheetStatements",
                "ordering": ["-created_at"],
            },
        ),
    ]
