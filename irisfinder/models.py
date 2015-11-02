from django.db import models
from picklefield.fields import PickledObjectField
import datetime

# Create your models here.

class Iris(models.Model):
    sepal_length = models.FloatField()
    sepal_width = models.FloatField()
    petal_length = models.FloatField()
    petal_width = models.FloatField()
    species = models.CharField(max_length=200)
    user_data = models.BooleanField(default=False)
    date_created = models.DateTimeField(null=False, default=datetime.datetime.now())


class SVMModels(models.Model):
    model_pickle = PickledObjectField()
    training_data_X = PickledObjectField()
    training_data_y = PickledObjectField()
    test_data_X = PickledObjectField()
    test_data_y = PickledObjectField()
    score = models.FloatField()
    random_state_int = models.IntegerField()
    test_size = models.FloatField()
    model_function_source = models.TextField()
    scikit_version = models.CharField(max_length=200)
    numpy_version = models.CharField(max_length=200)
    scipy_version = models.CharField(max_length=200)
    run_date = models.DateTimeField()
