# Generated by Django 2.2 on 2019-05-01 20:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190426_0628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 1, 20, 42, 28, 274128, tzinfo=utc)),
        ),
    ]
