# Generated by Django 2.0.1 on 2018-01-30 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classy', '0004_auto_20180130_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classification',
            name='classification_name',
            field=models.CharField(choices=[('Confidential', 'confidential'), ('Unclassified', 'unclassified'), ('PROTECTED A', 'protected a'), ('PROTECTED B', 'protected b')], default='confidential', max_length=50),
        ),
    ]
