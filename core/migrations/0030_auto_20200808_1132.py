# Generated by Django 2.2.8 on 2020-08-08 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_item_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='item',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='user',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]
