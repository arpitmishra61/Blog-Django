# Generated by Django 2.2.3 on 2019-07-11 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20190711_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='articles',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Article'),
        ),
    ]
