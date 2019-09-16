# Generated by Django 2.2.5 on 2019-09-16 18:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('api', '0009_item_barcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='barcode',
            field=models.CharField(blank=True, help_text='Frei lassen, um Barcode automatisch zu generieren',
                                   max_length=15, null=True, unique=True, verbose_name='Barcode'),
        ),
    ]
