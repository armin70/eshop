# Generated by Django 2.2.8 on 2020-08-06 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20200806_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='timestamp',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
