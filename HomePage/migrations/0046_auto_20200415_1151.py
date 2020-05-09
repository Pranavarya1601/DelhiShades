# Generated by Django 3.0.4 on 2020-04-15 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomePage', '0045_adminpost_blog_published_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminpost',
            name='blog_category',
            field=models.CharField(blank=True, choices=[('Architecture', 'Architecture'), ('Delhi Diary', 'Delhi Diary'), ('Events', 'Events'), ('Education', 'Education'), ('Fashion', 'Fashion'), ('Food', 'Food'), ('Health & Fitness', 'Health & Fitness'), ('History', 'History'), ('Lifestyle', 'Lifestyle'), ('News', 'News'), ('Shopping', 'Shopping'), ('Social Welfare', 'Social Welfare'), ('Places', 'Places'), ('Travel', 'Travel'), ('Technology', 'Technology'), ('Others', 'Others')], max_length=350),
        ),
    ]
