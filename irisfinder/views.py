from django.shortcuts import render
import datetime

# Create your views here.

def explore(request):
    data = {
        "app_name": "irisfinder",
        "current_date": datetime.datetime.now().strftime('%A, %B %d, %Y'),
        "current_time": datetime.datetime.now().strftime('%I:%M:%S %p')
    }
    return render(request, 'explore.html', context=data)