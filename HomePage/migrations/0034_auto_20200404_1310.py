# Generated by Django 3.0.4 on 2020-04-04 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomePage', '0033_auto_20200403_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='user_rating',
            field=models.CharField(blank=True, default='Bronze', max_length=100),
        ),
    ]