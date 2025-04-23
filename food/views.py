from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def biryani(request):
    return HttpResponse('Biryani tastes good')
def icecream(request):
    return HttpResponse('ice cream')
