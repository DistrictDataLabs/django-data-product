from django.shortcuts import render
import datetime
from models import Iris, SVMModels
from forms import UserIrisData
import sklearn
from sklearn import svm
from sklearn.cross_validation import train_test_split
import numpy as np
from django.conf import settings
import cPickle
import scipy
from pytz import timezone
import random

# Create your views here.

def predict(request):
    data = {
        "app_name": "irisfinder",
        "random_number": random.randint(0, 10000)
    }

    if request.method == "GET":
        form = UserIrisData()
        data.update({"form": form, "submit": True})
    elif request.method == "POST":
        form = UserIrisData(request.POST)
        sepal_length = request.POST.get("sepal_length")
        sepal_width = request.POST.get("sepal_width")
        petal_length = request.POST.get("petal_length")
        petal_width = request.POST.get("petal_width")
        if request.POST.get('submit'):
            user_data = Iris(user_data=True,
                             sepal_length=sepal_length,
                             sepal_width=sepal_width,
                             petal_length=petal_length,
                             petal_width=petal_width)
            user_data.save()
            model_object = SVMModels.objects.order_by("-run_date").first()
            model = cPickle.loads(model_object.model_pickle)
            prediction = model.predict([sepal_length, sepal_width, petal_length, petal_width])
            item_pk = user_data.pk
            species = prediction[0]
            data.update({"form": form, "verify": True, "item_pk": item_pk,
                         "species": species, "prediction": prediction[0]})
        elif request.POST.get('verified'):
            user_data = Iris.objects.get(pk=int(request.POST.get("item_pk")))
            user_data.species = request.POST.get("species")
            user_data.save()

    return render(request, "predict.html", context=data)