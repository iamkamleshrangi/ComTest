# Generated by Django 2.1.7 on 2019-03-31 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roc', '0004_auto_20190331_1123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='id',
        ),
        migrations.AlterField(
            model_name='company',
            name='cin_number',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
    ]