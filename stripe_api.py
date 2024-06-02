import stripe

class StripeApi():
    def __init__(self, api_key) -> None:
        stripe.api_key = api_key


    def create_product(self, product):
        try:
            stripe_product = stripe.Product.create(
                name=product.name,
                description="EXAMPLE",
                type='good'
            )
            return stripe_product.id
        except stripe.error.StripeError as e:
            raise
            
    def create_price(self, stripe_product_id, checkout_product_price):
        try:
            unit_amount = int(checkout_product_price * 100)
            
            stripe_price = stripe.Price.create(
                product=stripe_product_id,
                unit_amount=unit_amount,
                currency="usd"
            )
            return stripe_price.id
        except stripe.error.StripeError as e:
            raise