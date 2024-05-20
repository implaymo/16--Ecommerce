from django.shortcuts import render 
from api import Api
from polls.models import Product

def index(request):
    api = Api()
    api.get_all_products()

    try:
        for dictionary in api.all_products:
            Product.objects.create(name=dictionary["name"], price=dictionary["price"], description=dictionary["description"], image=dictionary["image"])
    except Exception as e:
        print(f"ERROR: {e}")
    
    return render(request, "index.html")