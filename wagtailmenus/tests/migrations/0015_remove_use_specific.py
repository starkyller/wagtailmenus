# Generated by Django 2.1.9 on 2019-07-10 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0014_noabsoluteurlspage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customflatmenu',
            name='use_specific',
        ),
        migrations.RemoveField(
            model_name='custommainmenu',
            name='use_specific',
        ),
    ]
