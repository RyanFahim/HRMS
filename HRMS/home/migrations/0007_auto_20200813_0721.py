# Generated by Django 3.1 on 2020-08-13 01:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20200813_0631'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Asset',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
