# Generated by Django 4.0.1 on 2023-04-24 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rider', '0012_order_totalpartysize'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='totalPartySize',
            field=models.PositiveIntegerField(),
        ),
    ]
