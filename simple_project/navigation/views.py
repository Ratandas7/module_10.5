from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def about(request):
    # return HttpResponse("This is about page")
    return render(request, 'about.html')

def contact(request):
    # return HttpResponse("This is contact page")
    return render(request, 'contact.html')