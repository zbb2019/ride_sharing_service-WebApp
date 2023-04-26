# Generated by Django 4.0.1 on 2023-04-16 01:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rider', '0009_alter_order_ownerpartysize'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='driverID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='rider.driver'),
        ),
        migrations.AlterField(
            model_name='order',
            name='sharerID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sharerID', to=settings.AUTH_USER_MODEL),
        ),
    ]