# Generated by Django 2.2.3 on 2019-07-11 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_auto_20190711_1804'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
        migrations.RemoveField(
            model_name='user',
            name='joinedAt',
        ),
        migrations.RemoveField(
            model_name='user',
            name='mobile',
        ),
        migrations.RemoveField(
            model_name='user',
            name='password',
        ),
    ]
