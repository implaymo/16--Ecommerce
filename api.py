import requests
import json

class Api():
    def __init__(self) -> None:
        self.url = "https://dummyjson.com/products"
        self.all_products = []
        

    def get_all_products(self):
        response = requests.get(self.url)
        data = response.json()
        total_products = data["products"]


        for i in range(len(total_products)):
            product_name = data["products"][i]["title"]
            product_price = data["products"][i]["price"]
            product_description = data["products"][i]["description"]
            product_image = data["products"][i]["thumbnail"]
            
            if product_name in self.all_products:
                continue
            else:
                self.all_products.append({
                    "name": product_name,
                    "price": product_price,
                    "description": product_description,
                    "image": product_image,
                })
        