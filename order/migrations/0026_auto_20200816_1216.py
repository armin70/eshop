# Generated by Django 2.2.8 on 2020-08-16 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0025_auto_20200816_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopcart',
            name='qr',
            field=models.BooleanField(default=False),
        ),
    ]
