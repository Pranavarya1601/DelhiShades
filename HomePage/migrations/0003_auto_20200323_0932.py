# Generated by Django 3.0 on 2020-03-23 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomePage', '0002_auto_20200322_1203'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='user_pic',
            new_name='profile_image',
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='age',
            field=models.DateField(blank=True),
        ),
    ]