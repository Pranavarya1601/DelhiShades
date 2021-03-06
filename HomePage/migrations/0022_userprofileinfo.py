# Generated by Django 3.0.4 on 2020-03-30 07:38

import HomePage.models
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('HomePage', '0021_delete_userprofileinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfileInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_gender', models.CharField(choices=[('Female', 'Female'), ('Male', 'Male'), ('Others', 'Others')], max_length=20)),
                ('user_age', models.DateField(blank=True, default=datetime.datetime.now)),
                ('user_profile_image', models.ImageField(blank=True, help_text='The images files size must be greater than 200kb and less than 500kb. The dimensions of the photograph should be 800 (width) x 800 (height)', upload_to='profile_image', validators=[HomePage.models.validate_image])),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
