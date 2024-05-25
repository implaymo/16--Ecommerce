class Db:
    def __init__(self) -> None:
        self.all_db_data = []
        
        
    def update(self,name, price, description, image, class_):
        class_.objects.create(name=name, price=price, description=description, image=image)

    def get_db_data(self,class_):
        db_data = class_.objects.all()
        for product in db_data:
            self.all_db_data.append(product.name)