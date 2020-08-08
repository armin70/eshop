# Generated by Django 2.2.8 on 2020-08-07 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_auto_20200807_1616'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'تگ', 'verbose_name_plural': 'تگ ها'},
        ),
        migrations.AddField(
            model_name='tag',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=250),
        ),
    ]
