# Generated by Django 2.2.8 on 2020-08-09 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_shopcart_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopcart',
            name='size',
            field=models.CharField(max_length=5, null=True),
        ),
    ]