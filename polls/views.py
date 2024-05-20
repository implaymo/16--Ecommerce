from django.shortcuts import render 
from api import Api

def index(request):
    return render(request, "index.html")