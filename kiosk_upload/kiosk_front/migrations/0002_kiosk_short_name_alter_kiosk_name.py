# Generated by Django 4.1.5 on 2023-02-02 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kiosk_front', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='kiosk',
            name='short_name',
            field=models.CharField(default='', max_length=45, unique=True, verbose_name='Kiosk short name'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='kiosk',
            name='name',
            field=models.CharField(max_length=45, unique=True, verbose_name='Kiosk name'),
        ),
    ]
