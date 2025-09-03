from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def biriyani(request):
    return HttpResponse('biriyani is very yummy')
def kabab(request):
    return HttpResponse('kabab is very yummy')
