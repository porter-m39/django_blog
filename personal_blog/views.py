#from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    #return HttpResponse("You're at the homepage.")
    return render(request, 'base.html')

def about(request):
    #return HttpResponse("Here's a bit about me.")
    return render(request, 'about.html')
