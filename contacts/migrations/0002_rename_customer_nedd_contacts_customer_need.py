# Generated by Django 4.0.4 on 2022-05-25 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contacts',
            old_name='customer_nedd',
            new_name='customer_need',
        ),
    ]
