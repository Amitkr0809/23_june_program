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
    def __init__(self,name,price,deal,rating,warranty):
        super().__init__(name,price,deal,rating)
        self.warranty=warranty
    def display_details(self):
        super().display_details()
        print("warranty {}".format(self.warranty))

class Grocery(Product):
    def __init__(self,name,price,deal,rating,expired):
        super().__init__(name,price,deal,rating)
        self.expired=expired
    def display_details(self):
        super().display_details()
        print("expired: {}".format(self.expired))

p=Electronic("Tv",40000,25000,4,24)
Milk=Grocery("Milk",36,30,4,"jan 2023")
p.display_details()
Milk.display_details()