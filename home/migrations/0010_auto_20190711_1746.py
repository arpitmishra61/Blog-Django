# Generated by Django 2.2.3 on 2019-07-11 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20190711_1738'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list',
            name='article',
        ),
        migrations.RemoveField(
            model_name='user',
            name='articles',
        ),
        migrations.DeleteModel(
            name='Article',
        ),
    ]
