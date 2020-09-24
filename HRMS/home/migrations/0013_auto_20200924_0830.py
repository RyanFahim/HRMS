# Generated by Django 3.1 on 2020-09-24 02:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20200924_0824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='salary',
            field=models.DecimalField(decimal_places=5, max_digits=100),
        ),
        migrations.CreateModel(
            name='Accountt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=1000)),
                ('month', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.month')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.employee')),
            ],
        ),
    ]
