# Generated by Django 3.2.5 on 2021-07-28 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_post_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='medicine',
            field=models.TextField(default='', max_length=200),
        ),
    ]
