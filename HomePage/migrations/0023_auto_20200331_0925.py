# Generated by Django 3.0.4 on 2020-03-31 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomePage', '0022_userprofileinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='user_gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=20),
        ),
    ]
