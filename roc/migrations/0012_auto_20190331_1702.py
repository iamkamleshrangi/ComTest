# Generated by Django 2.1.7 on 2019-03-31 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roc', '0011_auto_20190331_1646'),
    ]

    operations = [
        migrations.RenameField(
            model_name='director',
            old_name='din',
            new_name='din_dpin_pan',
        ),
    ]