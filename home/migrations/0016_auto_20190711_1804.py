# Generated by Django 2.2.3 on 2019-07-11 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20190711_1802'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='List',
        ),
    ]
