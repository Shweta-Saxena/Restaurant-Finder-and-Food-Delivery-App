# Generated by Django 3.0.5 on 2020-06-14 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaapp', '0002_customermodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=12)),
                ('phoneno', models.CharField(max_length=12)),
                ('address', models.CharField(max_length=120)),
                ('orderitems', models.CharField(max_length=12)),
            ],
        ),
    ]
