# Generated by Django 2.2.8 on 2020-08-07 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_auto_20200807_1653'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='slug',
        ),
    ]