# Generated by Django 2.2.8 on 2020-07-28 20:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20200729_0121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.ForeignKey(default='noCat', max_length=255, on_delete=django.db.models.deletion.CASCADE, to='core.Category'),
        ),
    ]
