# Generated by Django 2.2.3 on 2019-07-11 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_auto_20190711_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='articles',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='home.Article'),
        ),
        migrations.AlterField(
            model_name='user',
            name='list',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.List'),
        ),
    ]
