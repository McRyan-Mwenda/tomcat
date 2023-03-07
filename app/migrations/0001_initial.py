# Generated by Django 4.1.7 on 2023-03-07 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public_id', models.CharField(default='d7ac5c7d52684414bb8eeeb908dceb06', max_length=40)),
                ('account_name', models.CharField(max_length=100)),
                ('account_type', models.CharField(choices=[('checking', 'Checking'), ('saving', 'Saving'), ('credit', 'Credit'), ('investment', 'Investment'), ('retirement', 'Retirement'), ('loan', 'Loan'), ('insurance', 'Insurance'), ('mortgage', 'Mortgage')], default='checking', max_length=50)),
                ('currency_code', models.CharField(max_length=3)),
                ('account_balance', models.DecimalField(decimal_places=2, max_digits=15)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'account',
                'verbose_name_plural': 'accounts',
                'db_table': 'Accounts',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public_id', models.CharField(default='5b49eecb9be24e04816e788301e3a1bd', max_length=40)),
                ('budget_name', models.CharField(max_length=100)),
                ('budget_description', models.CharField(max_length=255)),
                ('budget_start_date', models.CharField(max_length=50)),
                ('budget_end_date', models.CharField(max_length=50)),
                ('budget_amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'budget',
                'verbose_name_plural': 'budgets',
                'db_table': 'Budgets',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='BudgetCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public_id', models.CharField(default='d87ae4d586e8473884417d93d4744049', max_length=40)),
            ],
            options={
                'verbose_name': 'budget category',
                'verbose_name_plural': 'budget categories',
                'db_table': 'BudgetCategories',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public_id', models.CharField(default='b3a1a90a41234e51a2454542b0cea3bf', max_length=40)),
                ('category_name', models.CharField(max_length=100)),
                ('category_description', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'db_table': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public_id', models.CharField(default='baa79f17840741efb8eabc87cb1f619b', max_length=40)),
                ('report_name', models.CharField(max_length=100)),
                ('report_description', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('accounts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.account')),
            ],
            options={
                'verbose_name': 'report',
                'verbose_name_plural': 'reports',
                'db_table': 'Reports',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public_id', models.CharField(default='4c8a3ee89f3e4ed8adb58caad39a98bd', max_length=40)),
                ('transaction_type', models.CharField(choices=[('deposit', 'Deposit'), ('withdrawal', 'Withdrawal'), ('transfer', 'Transfer'), ('payment', 'Payment')], max_length=50)),
                ('transaction_amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('currency_code', models.CharField(max_length=3)),
                ('description', models.CharField(max_length=255)),
                ('transaction_date', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.account')),
            ],
            options={
                'verbose_name': 'transaction',
                'verbose_name_plural': 'transactions',
                'db_table': 'Transactions',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='TransactionCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public_id', models.CharField(default='df9e1b00f9a446e48e08d92d3c25e4ec', max_length=40)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.category')),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.transaction')),
            ],
            options={
                'verbose_name': 'transaction category',
                'verbose_name_plural': 'transaction categories',
                'db_table': 'TransactionCategories',
            },
        ),
        migrations.CreateModel(
            name='ReportCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public_id', models.CharField(default='a444c4ebf18943ac91c811f0b8c1b63c', max_length=40)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.category')),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.report')),
            ],
            options={
                'verbose_name': 'report category',
                'verbose_name_plural': 'report categories',
                'db_table': 'ReportCategories',
            },
        ),
        migrations.AddField(
            model_name='report',
            name='transactions',
            field=models.ManyToManyField(to='app.transaction'),
        ),
    ]
