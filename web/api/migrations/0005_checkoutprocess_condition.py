# Generated by Django 2.2.5 on 2019-11-02 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('api', '0004_auto_20191102_1157'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkoutprocess',
            name='condition',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    to='api.CheckOutCondition', verbose_name='Check-Out-Bedingung'),
        ),
    ]
