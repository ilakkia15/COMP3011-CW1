from django.shortcuts import render
from django.http import HttpResponse
from .models import Professor, Module, Instance, Student, Rating
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def HandleRegisterRequest(request):
    return HttpResponse('Handled Register Request')
