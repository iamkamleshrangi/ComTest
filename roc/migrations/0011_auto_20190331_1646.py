# Generated by Django 2.1.7 on 2019-03-31 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roc', '0010_auto_20190331_1645'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='charge',
            new_name='charges',
        ),
    ]
