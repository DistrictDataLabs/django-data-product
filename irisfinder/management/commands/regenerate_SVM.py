from django.core.management.base import BaseCommand, CommandError

import datetime
import sklearn
import scipy
import numpy as np
from irisfinder.models import Iris, SVMModels
from sklearn import svm
from sklearn.cross_validation import train_test_split
from pytz import timezone
from django.conf import settings
import cPickle


class Command(BaseCommand):
    help = "Regenerates persisted SVM Models with current database data."

    def handle(self, *args, **kwargs):
        iris_data = Iris.objects.exclude(species=None)
        X_fields = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
        X_values = iris_data.values_list(*X_fields)
        y_values = iris_data.values_list('species', flat=True)
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

        # save model and metadata
        svm_model_object = SVMModels()
        svm_model_object.test_size = test_size
        svm_model_object.random_state_int = random_state_int
        svm_model_object.model_pickle = cPickle.dumps(model)
        svm_model_object.score = score
        svm_model_object.run_date = run_date
        svm_model_object.training_data_X, svm_model_object.training_data_y = cPickle.dumps(X_train), cPickle.dumps(
            y_train)
        svm_model_object.test_data_X, svm_model_object.test_data_y = cPickle.dumps(X_test), cPickle.dumps(y_test)
        svm_model_object.scikit_version = sklearn.__version__
        svm_model_object.numpy_version = np.__version__
        svm_model_object.scipy_version = scipy.__version__
        svm_model_object.save()
