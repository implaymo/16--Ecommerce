from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from polls.models import Product, Checkout
from database import Database
from searchbar import SearchBar
from django.contrib import messages
from api import Api
import logging
logger = logging.getLogger(__name__)

api = Api()
db = Database()
search_bar = SearchBar()


def compare_api_db_data():
    for dictionary in api.all_products:
        if dictionary["name"] in db.all_db_data:
            continue
        else:
            db.update(name=dictionary["name"], price=dictionary["price"], description=dictionary["description"], image=dictionary["image"], class_=Product)


def get_website_data():
    try: 
        api.get_all_products()
        db.get_all_db_data(class_=Product)
        compare_api_db_data()
    except Exception as e:
        print(f"ERROR: {e}")
        
def index(request):
    get_website_data()
        
    db_data = Product.objects.all()
    
    context = {
        'db_data': db_data,
    }    
    return render(request, "index.html",context=context)

def search(request):
    query_name = search_bar.get_search_input(request=request)
    db_data = db.get_search_product(class_=Product, query_name=query_name)
    if db_data:
        context = {
            'db_data': db_data 
            }    
        return render(request, "index.html", context=context)
    else:
        messages.info(request, "Item doensn't exist")
        return redirect('index')
    
def add_to_cart(request):
    logger.info(f"Request method: {request.method}")
    if request.method == "POST":
        product_id = request.POST.get('product_id')
        logger.info(f"Product ID: {product_id}")
        try:
            product = get_object_or_404(Product, id=product_id)        
            db.add_checkout_product(class_=Checkout, name=product.name, price=product.price)
            checkout_products = db.get_checkout_product(class_=Checkout)

            response_data = {
                'message': 'Product added to cart',
                'checkout_products': list(checkout_products.values()),  
            }
            return JsonResponse(response_data)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    
    return JsonResponse({'error': 'Invalid request'}, status=400)

def delete_cart(request):
    Checkout.objects.all().delete()
    return redirect('index')
