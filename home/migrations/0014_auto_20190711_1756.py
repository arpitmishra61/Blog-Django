# Generated by Django 2.2.3 on 2019-07-11 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20190711_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='articles',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Article'),
        ),
        migrations.AlterField(
            model_name='user',
            name='list',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.List'),
        ),
    ]
