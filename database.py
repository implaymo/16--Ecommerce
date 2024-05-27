class Database:
    def __init__(self) -> None:
        self.all_db_data = []
        
        
    def update(self,name, price, description, image, class_):
        class_.objects.create(name=name, price=price, description=description, image=image)

    def get_all_db_data(self,class_):
        db_data = class_.objects.all()
        for product in db_data:
            self.all_db_data.append(product.name)
            
    def get_search_product(self, query_name, class_):
        search_product = class_.objects.filter(name__contains=query_name)
        return search_product
    
    def add_checkout_product(self, name, price, class_):
        class_.objects.create(name=name, price=price)
        
    def get_checkout_product(self, class_):
        db_data = class_.objects.all()
        return db_data