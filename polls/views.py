from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from polls.models import Product, Checkout
from database import Database
from django.contrib import messages
from api import Api
from stripe_api import StripeApi
import stripe
import os
from dotenv import load_dotenv
import logging

load_dotenv()
logger = logging.getLogger(__name__)

api = Api()
db = Database()
stripe_api = StripeApi(api_key=os.getenv("STRIPE_PRIVATE_KEY") )


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
        
def bill():
    checkout_products = Checkout.objects.all()
    all_price = [product.price for product in checkout_products]
    total = sum(all_price)
    return total

    
def index(request):
    
    get_website_data()       
    db_data = Product.objects.all()
    checkout_products = Checkout.objects.all()

    try:
        all_price = [product.price for product in checkout_products]
        total = sum(all_price)
    except UnboundLocalError:
        print(f"ERROR {UnboundLocalError}")
    
    context = {
        'db_data': db_data,
        'checkout_products': checkout_products,
        'bill': total
    }    
    return render(request, "index.html", context=context)


def search(request):
    product_searched = request.POST.get('search_query')
    db_data = db.get_search_product(class_=Product, query_name=product_searched)
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
    if request.method == "POST":
        try:
            Checkout.objects.all().delete()
            response_data = {
                'success': True
            }
            return JsonResponse(response_data)
        except Exception as e:
            print(f"Error: {e}")
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid request'}, status=400)

def delete_item(request):
    logger.info(f"Request method: {request.method}")
    if request.method == "POST":
        product_id = request.POST.get('product_id')
        try:
            cart_item = get_object_or_404(Checkout, id=product_id)
            cart_item.delete()
            checkout_products = db.get_checkout_product(class_=Checkout)
            response_data = {
                            'success': True,
                            'checkout_products': list(checkout_products.values()),  
                        }
            return JsonResponse(response_data)
        except Exception as e:
            logger.error(f"Error deleting item: {e}")
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid request'}, status=400)

def update_bill(request):
    if request.method == "GET":
        try:
            total = bill()
            return JsonResponse({'bill': round(total, 2)})
        except Exception as e:
            logger.error(f'Error: {e}')
            
def checkout(request):
    if request.method == "GET":
        line_items = []
        checkout_products = Checkout.objects.all()
        
        for product in checkout_products:
            stripe_product_id = stripe_api.create_product(product=product)
            stripe_price_id = stripe_api.create_price(stripe_product_id=stripe_product_id, checkout_product_price=product.price)
            
            line_items.append({
                'price': stripe_price_id,
                'quantity': 1  
            })

        try:
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=[
                    'card', 
                    'paypal'
                ],
                line_items=line_items,
                mode='payment',
                success_url='http://127.0.0.1:8000' + '/success_checkout/',
                cancel_url='http://127.0.0.1:8000' + '/cancel_checkout/',
            )
            return redirect(checkout_session.url)
        except stripe.error.StripeError as e:
            print(f"Stripe error: {e}")
            return HttpResponse("No item in the cart. Add an item to checkout.", status=500)
        except Exception as e:
            print(f"General error: {e}")
            return HttpResponse("An unexpected error occurred.", status=500)
    else:
        return HttpResponse("Invalid request method.", status=405)


def cancel_checkout(request):
    return render(request, 'cancel.html')

def success_checkout(request):
    return render(request, 'success.html')
