# Generated by Django 3.0.4 on 2020-03-28 06:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomePage', '0012_userpostmessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpostmessage',
            name='user_post_date',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
    ]