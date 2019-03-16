# Generated by Django 2.1.5 on 2019-03-16 16:43

import api.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('api', '0003_auto_20190316_1740'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='location',
            options={'verbose_name': 'Ort', 'verbose_name_plural': 'Orte'},
        ),
        migrations.AlterModelOptions(
            name='preset',
            options={'verbose_name': 'Preset', 'verbose_name_plural': 'Presets'},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='location',
            name='number',
            field=models.IntegerField(blank=True, unique=True, verbose_name='Schranknummer'),
        ),
        migrations.AlterField(
            model_name='preset',
            name='category',
            field=models.ForeignKey(default=api.models.default_preset, on_delete=django.db.models.deletion.SET_DEFAULT,
                                    to='api.Category', verbose_name='Kategorie'),
        ),
        migrations.AlterField(
            model_name='preset',
            name='description',
            field=models.TextField(blank=True, verbose_name='Beschreibung'),
        ),
        migrations.AlterField(
            model_name='preset',
            name='manufacturer',
            field=models.CharField(blank=True, max_length=100, verbose_name='Hersteller'),
        ),
        migrations.AlterField(
            model_name='preset',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Bezeichnung'),
        ),
    ]
