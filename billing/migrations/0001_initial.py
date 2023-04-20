# Generated by Django 4.1.7 on 2023-04-20 04:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PlanBilling',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_tracking_id', models.CharField(max_length=200)),
                ('merchant_ref', models.CharField(max_length=50)),
                ('account_ref', models.CharField(blank=True, max_length=50)),
                ('redirect_url', models.URLField()),
                ('plan', models.CharField(max_length=10)),
                ('currency', models.CharField(max_length=5)),
                ('amount', models.FloatField(default=0.0)),
                ('payment_confirmed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'subscription payment',
                'verbose_name_plural': 'subscription payments',
                'db_table': 'SubscriptionPayments',
                'ordering': ['-created_at'],
            },
        ),
    ]
