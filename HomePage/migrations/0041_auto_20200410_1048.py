# Generated by Django 3.0.4 on 2020-04-10 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomePage', '0040_auto_20200410_1044'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adminpost',
            old_name='category',
            new_name='blog_category',
        ),
        migrations.AlterField(
            model_name='adminpost',
            name='blog_photo_1',
            field=models.ImageField(blank=True, upload_to='AdminPost'),
        ),
        migrations.AlterField(
            model_name='adminpost',
            name='blog_photo_2',
            field=models.ImageField(blank=True, upload_to='AdminPost'),
        ),
        migrations.AlterField(
            model_name='adminpost',
            name='blog_photo_3',
            field=models.ImageField(blank=True, upload_to='AdminPost'),
        ),
        migrations.AlterField(
            model_name='adminpost',
            name='blog_photo_4',
            field=models.ImageField(blank=True, upload_to='AdminPost'),
        ),
    ]
