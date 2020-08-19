# Generated by Django 3.1 on 2020-08-12 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_product_catergory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Postion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('emp_code', models.CharField(max_length=5)),
                ('email', models.EmailField(max_length=100)),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.postion')),
            ],
        ),
    ]
