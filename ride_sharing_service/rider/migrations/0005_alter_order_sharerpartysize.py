# Generated by Django 4.0.1 on 2023-04-14 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rider', '0004_rename_reqarrvtime_order_reqarrvdatetime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='sharerPartySize',
            field=models.PositiveIntegerField(blank=True, default=1),
        ),
    ]
