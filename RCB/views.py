from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Captain(request):
    return HttpResponse('<h1> kohli is the captain of rcb</h1>')
