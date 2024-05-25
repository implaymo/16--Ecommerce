from django.shortcuts import render
from api import Api
from polls.models import Product
from database import Database
from searchbar import SearchBar


api = Api()
db = Database()
search_bar = SearchBar()


def compare_api_db_data():
    for dictionary in api.all_products:
        if dictionary["name"] in db.all_db_data:
            continue
        else:
            db.update(name=dictionary["name"], price=dictionary["price"], description=dictionary["description"], image=dictionary["image"], class_=Product)

def index(request):
    try: 
        api.get_all_products()
        db.get_all_db_data(class_=Product)
        compare_api_db_data()
    except Exception as e:
        print(f"ERROR: {e}")
        
    db_data = Product.objects.all()
    
    context = {
        'db_data': db_data
    }    
    return render(request, "index.html",context=context)

def search(request):
    query_name = search_bar.get_search_input(request=request)
    db_data = db.get_search_product(class_=Product, query_name=query_name)
    context = {
        'db_data': db_data
    }    
    return render(request, "index.html", context=context)

