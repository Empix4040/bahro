# Generated by Django 3.1.6 on 2021-11-29 19:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_auto_20211114_0138'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.CharField(default=datetime.datetime(2021, 11, 29, 19, 49, 45, 929754, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]
