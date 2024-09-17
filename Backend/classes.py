class product:
    def __init__(self, product_id, product_name, preis, hersteller_id):
        self.product_id = product_id
        self.product_name = product_name
        self.preis = preis
        self.hersteller_id = hersteller_id
    def showobject(self):
        return f"{self.product_id}, {self.product_name}"
    