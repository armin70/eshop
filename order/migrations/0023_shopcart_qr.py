# Generated by Django 2.2.8 on 2020-08-15 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0022_order_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopcart',
            name='qr',
            field=models.BooleanField(null=True),
        ),
    ]
