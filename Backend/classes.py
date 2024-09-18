class product:
    def __init__(self, product_id, product, price, manufacturer_id):
        self.product_id = product_id
        self.product = product
        self.price = price
        self.manufacturer_id = manufacturer_id
    def showobject(self):
        return f"{self.product_id}, {self.product_name}, {self.manufacturer_id}"
    

class manufacturer:
    def __init__(self, manufacturer_id, manufacturer, country_id):
        self.manufacturer_id = manufacturer_id
        self.manufacturer = manufacturer
        self.country_id = country_id
    def showobject(self):
        return f"{self.manufacturer_id}, {self.manufacturer_name}, {self.country_id}"
    
class country:
    def __init__(self, country_id, country):
        self.country_id = country_id
        self.country = country
    def showobject(self):
        return f"{self.country_id}, {self.country}"