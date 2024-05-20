from django.shortcuts import render 
from api import Api

def index(request):
    api = Api()

    api.get_all_products()
    
    return render(request, "index.html")