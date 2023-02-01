# Generated by Django 4.1.5 on 2023-02-01 13:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies: list[tuple[str, str]] = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cinema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, verbose_name='Cinema name')),
                ('city', models.CharField(max_length=45, verbose_name='City')),
                ('slug', models.SlugField(allow_unicode=True, max_length=45, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Cinema',
                'verbose_name_plural': 'Cinemas',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Kiosk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, verbose_name='Kiosk name')),
                ('ip', models.GenericIPAddressField(blank=True, null=True, verbose_name='IP адрес киоска')),
                ('is_enabled', models.BooleanField(default=True, verbose_name='Enabled')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('cinema', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='kiosks', to='kiosk_front.cinema')),
            ],
            options={
                'verbose_name': 'Kiosk',
                'verbose_name_plural': 'Kiosks',
                'ordering': ('name',),
            },
        ),
    ]
