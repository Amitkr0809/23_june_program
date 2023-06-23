class Product:
    def __init__(self,name,price,deal,rating):
        self.name=name
        self.price=price
        self.deal=deal
        self.rating=rating
        self.you_save=price-deal
    def display_details(self):
        print("Product: {}".format(self.name))
        print("Price: {}".format(self.price))
        print("Deal: {}".format(self.deal))
        print("Rating: {}".format(self.rating))
        print("You save: {}".format(self.you_save))

class Electronic(Product):
    pass

p=Electronic("Tv",40000,25000,4)
p.display_details()
