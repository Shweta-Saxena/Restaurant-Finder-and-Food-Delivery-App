# Generated by Django 3.0.5 on 2020-06-15 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaapp', '0004_auto_20200614_0458'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ordermodel',
            old_name='orderitems',
            new_name='ordereditems',
        ),
    ]