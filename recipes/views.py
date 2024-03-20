from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'recipes/home.html', context={
        'name' : 'José Henrique',
    })

def sobre(request):
    return HttpResponse('SOBRE')

def contato(request):
    return render(request, 'me-apague/temp.html' )