# Generated by Django 3.0.4 on 2020-03-29 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomePage', '0015_auto_20200328_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='age',
            field=models.DateField(blank=True, help_text='YYYY-MM-DD format', null=True),
        ),
    ]
