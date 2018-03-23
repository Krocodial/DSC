# Generated by Django 2.0.1 on 2018-03-05 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classy', '0014_auto_20180302_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='classification',
            name='state',
            field=models.CharField(choices=[('Active', 0), ('Inactive', 1), ('Pending Review', 2)], max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='classification_logs',
            name='state',
            field=models.CharField(choices=[('Active', 0), ('Inactive', 1)], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='classification',
            name='classification_name',
            field=models.CharField(choices=[('Unclassified', 'unclassified'), ('PUBLIC', 'public'), ('CONFIDENTIAL', 'confidential'), ('PROTECTED A', 'protected_a'), ('PROTECTED B', 'protected_b'), ('PROTECTED C', 'protected_c')], default='unclassified', max_length=50),
        ),
    ]