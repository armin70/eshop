# Generated by Django 2.2.8 on 2020-08-15 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0037_auto_20200816_0003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='qr',
        ),
    ]
