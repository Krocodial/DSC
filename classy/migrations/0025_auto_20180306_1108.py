# Generated by Django 2.0.1 on 2018-03-06 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classy', '0024_auto_20180306_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classification_logs',
            name='action_flag',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='classification_logs',
            name='classy_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='classification_review',
            name='action_flag',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='classification_review',
            name='classy_id',
            field=models.IntegerField(),
        ),
    ]
