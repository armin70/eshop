# Generated by Django 2.2.8 on 2020-08-11 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0016_delete_checkout'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopcart',
            name='amount',
            field=models.IntegerField(null=True),
        ),
    ]