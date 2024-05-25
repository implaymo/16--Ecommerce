from django.shortcuts import render
from api import Api
from polls.models import Product
from database import Db


api = Api()
db = Db()


def compare_api_db_data():
    for dictionary in api.all_products:
        if dictionary["name"] in db.all_db_data:
            continue
        else:
            db.update(name=dictionary["name"], price=dictionary["price"], description=dictionary["description"], image=dictionary["image"], class_=Product)

def index(request):
    try: 
        api.get_all_products()
        db.get_db_data(class_=Product)
        compare_api_db_data()
    except Exception as e:
        print(f"ERROR: {e}")
        
    db_data = Product.objects.all()
    
    context = {
        'db_data': db_data
    }    
    return render(request, "index.html",context=context)


