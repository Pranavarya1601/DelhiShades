# Generated by Django 3.0.4 on 2020-03-30 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HomePage', '0018_auto_20200329_1939'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='user_first_name',
        ),
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='user_last_name',
        ),
    ]
