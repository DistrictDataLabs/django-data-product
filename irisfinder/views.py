from django.shortcuts import render
import datetime
from models import Iris

# Create your views here.

def explore(request):
    data = {
        "app_name": "irisfinder",
        "current_date": datetime.datetime.now().strftime('%A, %B %d, %Y'),
        "current_time": datetime.datetime.now().strftime('%I:%M:%S %p')
    }
    iris_data = Iris.objects.all()
    data.update({"iris_data": iris_data})
    return render(request, 'explore.html', context=data)