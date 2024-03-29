# Generated by Django 5.0.1 on 2024-02-08 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_alter_car_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='price_per_day',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='price_per_hour',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='price_per_month',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
