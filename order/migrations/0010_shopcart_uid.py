# Generated by Django 2.2.8 on 2020-08-11 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0009_shopcart_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopcart',
            name='uid',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
