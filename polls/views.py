from django.shortcuts import render 
from api import Api
from polls.models import Product


api = Api()
all_db_data = []



def update_db(name, price, description, image):
        Product.objects.create(name=name, price=price, description=description, image=image)

def get_db_data():
    db_data = Product.objects.all()
    for product in db_data:
        all_db_data.append(product.name)

def compare_api_db_data():
    for dictionary in api.db_data:
        if dictionary["name"] in all_db_data:
            continue
        else:
            update_db(name=dictionary["name"], price=dictionary["price"], description=dictionary["description"], image=dictionary["image"])

def index(request):
    try: 
        api.get_all_products()
        get_db_data()
        compare_api_db_data()
    except Exception as e:
        print(f"ERROR: {e}")
        
    db_data = Product.objects.all()
    
    context = {
        'db_data': db_data
    }    
    return render(request, "index.html",context=context)