from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("DataFlair Django Tutorial<html><body><h1> Hello World DataFlair Dango tutorials</body></html>")

def nathan(request):
    return render(request, 'glebu/index.html')
