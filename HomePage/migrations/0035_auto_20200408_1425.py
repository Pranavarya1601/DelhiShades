# Generated by Django 3.0.4 on 2020-04-08 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomePage', '0034_auto_20200404_1310'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blog_published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='blog_heading',
            field=models.TextField(),
        ),
    ]
