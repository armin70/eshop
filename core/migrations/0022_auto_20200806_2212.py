# Generated by Django 2.2.8 on 2020-08-06 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_auto_20200806_2211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactus',
            name='tel',
        ),
        migrations.AddField(
            model_name='contactus',
            name='subject',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]