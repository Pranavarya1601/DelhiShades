# Generated by Django 3.0 on 2020-03-26 05:01

import HomePage.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomePage', '0008_fashion_food_travel_vlog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='user_photo',
            field=models.ImageField(blank=True, upload_to='events', validators=[HomePage.models.validate_image]),
        ),
        migrations.AlterField(
            model_name='fashion',
            name='user_photo',
            field=models.ImageField(blank=True, upload_to='fashion', validators=[HomePage.models.validate_image]),
        ),
        migrations.AlterField(
            model_name='food',
            name='user_photo',
            field=models.ImageField(blank=True, upload_to='food', validators=[HomePage.models.validate_image]),
        ),
        migrations.AlterField(
            model_name='travel',
            name='user_photo',
            field=models.ImageField(blank=True, upload_to='travel', validators=[HomePage.models.validate_image]),
        ),
        migrations.AlterField(
            model_name='vlog',
            name='user_photo',
            field=models.ImageField(blank=True, upload_to='vlog', validators=[HomePage.models.validate_image]),
        ),
    ]
