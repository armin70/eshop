# Generated by Django 2.2.8 on 2020-08-06 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_auto_20200806_2208'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactus',
            name='subject',
        ),
        migrations.AddField(
            model_name='contactus',
            name='tel',
            field=models.CharField(blank=True, max_length=17, null=True),
        ),
    ]