# Generated by Django 2.2.5 on 2019-10-12 14:58

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='checkoutprocess',
            options={'permissions': [('check_out', 'Can check out things'), ('check_in', 'Can check in things')],
                     'verbose_name': 'Check-Out-Vorgang', 'verbose_name_plural': 'Check-Out-Vorgänge'},
        ),
    ]
