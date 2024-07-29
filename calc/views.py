from django.http import QueryDict
from django.shortcuts import render


def calc(request):
    if request.method == 'POST':
        print('There is a POST-request')
        print(request.POST)
    return render(request, 'calc.html')


def about(request):
    return render(request, 'about.html')
