# Generated by Django 3.1 on 2020-09-02 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='company_head',
            new_name='head',
        ),
        migrations.RenameField(
            model_name='company',
            old_name='company_name',
            new_name='name',
        ),
    ]