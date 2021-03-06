# Generated by Django 2.2.8 on 2020-08-31 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0029_auto_20200828_1425'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=4000)),
                ('name', models.CharField(max_length=500)),
                ('zip_code', models.CharField(max_length=500)),
                ('tel', models.CharField(max_length=17)),
                ('address', models.TextField()),
                ('familiar', models.CharField(blank=True, max_length=2000, null=True)),
                ('criticism', models.CharField(blank=True, max_length=2000, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='total',
        ),
    ]
