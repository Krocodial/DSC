# Generated by Django 2.0.1 on 2018-02-06 17:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('classy', '0005_auto_20180130_1838'),
    ]

    operations = [
        migrations.AddField(
            model_name='classification',
            name='creation_date',
            field=models.DateField(default=datetime.datetime(2018, 2, 6, 17, 11, 15, 330653, tzinfo=utc)),
        ),
    ]