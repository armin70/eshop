# Generated by Django 2.2.8 on 2020-07-28 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20200729_0119'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.CharField(default='noCat', max_length=255),
        ),
    ]
