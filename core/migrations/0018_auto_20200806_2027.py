# Generated by Django 2.2.8 on 2020-08-06 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20200806_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
