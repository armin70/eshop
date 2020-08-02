# Generated by Django 2.2.8 on 2020-07-30 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20200730_0015'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('item', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.Item')),
            ],
        ),
    ]
