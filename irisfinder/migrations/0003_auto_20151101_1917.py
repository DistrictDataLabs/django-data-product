# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):
    dependencies = [
        ('irisfinder', '0002_svmmodels'),
    ]

    operations = [
        migrations.AddField(
            model_name='iris',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 1, 19, 17, 43, 688755)),
        ),
        migrations.AddField(
            model_name='iris',
            name='user_data',
            field=models.BooleanField(default=False),
        ),
    ]
