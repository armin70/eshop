# Generated by Django 2.2.8 on 2020-08-16 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0042_remove_producttype_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producttype',
            name='model',
        ),
        migrations.AddField(
            model_name='product',
            name='count',
            field=models.CharField(choices=[('single', 'single'), ('set', 'set'), ('family', 'family')], default='single', max_length=200),
        ),
    ]
