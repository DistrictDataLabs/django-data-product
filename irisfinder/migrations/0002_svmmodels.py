# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import picklefield.fields


class Migration(migrations.Migration):
    dependencies = [
        ('irisfinder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SVMModels',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('model_pickle', picklefield.fields.PickledObjectField(editable=False)),
                ('training_data_X', picklefield.fields.PickledObjectField(editable=False)),
                ('training_data_y', picklefield.fields.PickledObjectField(editable=False)),
                ('test_data_X', picklefield.fields.PickledObjectField(editable=False)),
                ('test_data_y', picklefield.fields.PickledObjectField(editable=False)),
                ('score', models.FloatField()),
                ('random_state_int', models.IntegerField()),
                ('test_size', models.FloatField()),
                ('model_function_source', models.TextField()),
                ('scikit_version', models.CharField(max_length=200)),
                ('numpy_version', models.CharField(max_length=200)),
                ('scipy_version', models.CharField(max_length=200)),
                ('run_date', models.DateTimeField()),
            ],
        ),
    ]
