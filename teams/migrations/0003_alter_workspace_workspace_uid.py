# Generated by Django 4.1.7 on 2023-04-19 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workspace',
            name='workspace_uid',
            field=models.CharField(default='ac15d376f09243609d95fa6ce1c47156', max_length=50),
        ),
    ]
