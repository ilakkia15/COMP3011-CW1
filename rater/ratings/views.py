from django.shortcuts import render
from django.http import HttpResponse
from .models import Professor, Module, Instance, Student, Rating

# Create your views here.

def Register(request):
    return HttpResponse('Handled Register Request')
