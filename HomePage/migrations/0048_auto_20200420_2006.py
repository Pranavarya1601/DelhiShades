# Generated by Django 3.0.4 on 2020-04-20 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomePage', '0047_auto_20200420_1124'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='facebook_link',
        ),
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='instagram_link',
        ),
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='twitter_link',
        ),
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='website_link',
        ),
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='youtube_link',
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='user_profile_image',
            field=models.ImageField(blank=True, upload_to='profile_image'),
        ),
    ]