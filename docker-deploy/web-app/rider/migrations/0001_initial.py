# Generated by Django 4.0.1 on 2023-04-05 02:21

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
            name='RideRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=100)),
                ('sharableTF', models.BooleanField()),
                ('destAddr', models.TextField()),
                ('reqArrvTime', models.CharField(max_length=100)),
                ('ownerPartySize', models.PositiveIntegerField()),
                ('vehicleType', models.CharField(blank=True, max_length=100)),
                ('specialRequest', models.TextField(blank=True)),
                ('ownerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
