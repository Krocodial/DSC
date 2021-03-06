# Generated by Django 2.0.1 on 2018-01-30 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classy', '0002_delete_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classification',
            name='classifier',
        ),
        migrations.AddField(
            model_name='classification',
            name='category',
            field=models.CharField(default='sensitive', max_length=40),
        ),
        migrations.AddField(
            model_name='classification',
            name='classification_name',
            field=models.CharField(choices=[('Confidential', 'confidential'), ('Unclassified', 'unclassified'), ('PROTECTED A', 'protected a'), ('PROTECTED B', 'protected b')], default='confidential', max_length=20),
        ),
        migrations.AddField(
            model_name='classification',
            name='column_name',
            field=models.CharField(default='not_provided', max_length=50),
        ),
        migrations.AddField(
            model_name='classification',
            name='datasource_description',
            field=models.CharField(default='not_provided', max_length=200),
        ),
        migrations.AddField(
            model_name='classification',
            name='schema',
            field=models.CharField(default='not_provided', max_length=50),
        ),
        migrations.AddField(
            model_name='classification',
            name='table_name',
            field=models.CharField(default='not_provided', max_length=50),
        ),
    ]
