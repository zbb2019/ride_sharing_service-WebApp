# Generated by Django 4.0.1 on 2023-04-22 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rider', '0011_alter_driver_userid'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='totalPartySize',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
