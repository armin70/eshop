# Generated by Django 2.2.8 on 2020-08-11 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0017_shopcart_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopcart',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]
