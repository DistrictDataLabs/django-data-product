from django.shortcuts import render
import datetime
from models import Iris
from sklearn import svm
from sklearn.cross_validation import train_test_split

# Create your views here.

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

    X_train, X_test, y_train, y_test = train_test_split(X_values, y_values, test_size=.4)

    clf = svm.SVC()
    model = clf.fit(X_values, y_values)
    score = clf.score(X_test, y_test)
    data.update({"model": model, "score": score})

    prediction = clf.predict([[5.3, 5.6, 8.9, 9.0]])
    data.update({"prediction": prediction})

    return render(request, 'explore.html', context=data)
