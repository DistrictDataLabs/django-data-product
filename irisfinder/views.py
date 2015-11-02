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
        data.update({"form": form})

    return render(request, "predict.html", context=data)

def explore(request):
    data = {
        "app_name": "irisfinder",
        "current_date": datetime.datetime.now().strftime('%A, %B %d, %Y'),
        "current_time": datetime.datetime.now().strftime('%I:%M:%S %p')
    }
    iris_data = Iris.objects.all()
    X_fields = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
    X_values = iris_data.values_list(*X_fields)
    y_values = iris_data.values_list('species', flat=True)
    data.update({"X": X_values, "Y": y_values})
    test_size = 0.4
    random_state_int = np.random.randint(1000)
    X_train, X_test, y_train, y_test = train_test_split(X_values,
                                                        y_values,
                                                        test_size=test_size,
                                                        random_state=random_state_int)
    clf = svm.SVC()
    model = clf.fit(X_values, y_values)
    run_date = datetime.datetime.now(tz=timezone(settings.TIME_ZONE))
    score = clf.score(X_test, y_test)
    data.update({"model": model, "score": score})

    prediction = clf.predict([[5.3, 5.6, 8.9, 9.0]])
    data.update({"prediction": prediction})

    # save model and metadata
    svm_model_object = SVMModels()
    svm_model_object.test_size = test_size
    svm_model_object.random_state_int = random_state_int
    svm_model_object.model_pickle = cPickle.dumps(model)
    svm_model_object.score = score
    svm_model_object.run_date = run_date
    svm_model_object.training_data_X, svm_model_object.training_data_y = cPickle.dumps(X_train), cPickle.dumps(y_train)
    svm_model_object.test_data_X, svm_model_object.test_data_y = cPickle.dumps(X_test), cPickle.dumps(y_test)
    svm_model_object.scikit_version = sklearn.__version__
    svm_model_object.numpy_version = np.__version__
    svm_model_object.scipy_version = scipy.__version__
    svm_model_object.save()

    return render(request, 'explore.html', context=data)
