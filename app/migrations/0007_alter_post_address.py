# Generated by Django 3.2.5 on 2021-07-28 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20210728_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='address',
            field=models.TextField(),
        ),
    ]
