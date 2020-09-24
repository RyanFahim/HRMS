# Generated by Django 3.1 on 2020-09-24 01:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_cvinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Month',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary', models.DecimalField(decimal_places=2, max_digits=100)),
                ('month', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.month')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.employee')),
            ],
        ),
    ]