# Generated by Django 2.2.8 on 2020-08-05 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='desc',
            field=models.CharField(blank=True, max_length=2500),
        ),
    ]
