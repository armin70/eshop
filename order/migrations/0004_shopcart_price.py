# Generated by Django 2.2.8 on 2020-08-08 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_remove_shopcart_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopcart',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]
