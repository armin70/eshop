# Generated by Django 2.2.8 on 2020-08-12 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0021_auto_20200813_0126'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.IntegerField(default=0),
        ),
    ]
