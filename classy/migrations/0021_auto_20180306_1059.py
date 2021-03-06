# Generated by Django 2.0.1 on 2018-03-06 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classy', '0020_auto_20180306_1058'),
    ]

    operations = [
        migrations.AddField(
            model_name='classification_logs',
            name='action_flag',
            field=models.SmallIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='classification_logs',
            name='classy_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='classification_review',
            name='classy_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
