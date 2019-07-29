# Generated by Django 2.2.3 on 2019-07-12 09:32

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0023_user_last_login'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=24)),
                ('mobile', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=100)),
                ('joinedAt', models.DateTimeField(default=datetime.datetime.now)),
                ('last_login', models.DateTimeField(default=datetime.datetime.now)),
                ('articles', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Article')),
                ('list', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.List')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='user',
        ),
    ]