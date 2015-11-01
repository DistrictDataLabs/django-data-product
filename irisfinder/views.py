from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def explore(request):
    return render(request, 'explore.html')