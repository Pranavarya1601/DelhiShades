# Generated by Django 3.0 on 2020-03-25 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomePage', '0004_auto_20200323_0947'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_photo', models.ImageField(blank=True, upload_to='events')),
                ('category', models.CharField(max_length=250)),
                ('heading', models.CharField(max_length=250)),
                ('paragraph', models.TextField()),
                ('user_name', models.CharField(max_length=250)),
                ('upload_date', models.DateField()),
            ],
        ),
    ]
