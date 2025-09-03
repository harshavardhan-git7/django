from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def chips(request):
    return HttpResponse('chips is ver yummy')
def dairymilk(request):
    return HttpResponse('dairymilk is ver sweet')