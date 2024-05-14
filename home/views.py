from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

def home(request):
    data = [
        {'name': 'Asad', 'age': 24},
        {'name': 'Zaheer', 'age': 25},
        {'name': 'Nouman', 'age': 26},
    ]

    return render(request, 'index.html', context={'data': data})