# from django.http import HttpResponse

from django.shortcuts import render

import datetime


# def home(request):
#     return HttpResponse("This is home page")


def home(request):

    d = {'author' : 'ovi', 'age' : 25, 'ex1' : 'chained', 'courses' : [
        {
            'name' : 'Python',
            'fee' : 20000
        },
        {
            'name' : 'Django',
            'fee' : 25000
        },
        {
            'name' : 'JavaScript',
            'fee' : 15000
        }
    ], 'ex2' : ['a', 'b', 'c', 'd'], 'ex3' : 5, 'ex4' : "I'm ovi", 'ex5' : "ovi", 'ex6' : "Ovi das", 'ex7' : "It is use cut", 'ex8' : datetime.datetime.now(), 'ex9' : '', 'ex10' : 123456789}

    return render(request, 'home.html', d)