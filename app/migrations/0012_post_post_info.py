# Generated by Django 3.2.5 on 2021-07-29 21:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_post_expiry_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_info',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]