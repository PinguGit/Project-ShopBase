class product:
    def __init__(self, product_id, product, price, manufacturer_id):
        self.product_id = product_id
        self.product = product
        self.price = price
        self.manufacturer_id = manufacturer_id
    def showobject(self):
        return f"{self.product_id}, {self.product}, {self.manufacturer_id}"
     

class manufacturer:
    def __init__(self, manufacturer_id, manufacturer, country_id):
        self.manufacturer_id = manufacturer_id
        self.manufacturer = manufacturer
        self.country_id = country_id
    def showobject(self):
        return f"{self.manufacturer_id}, {self.manufacturer}, {self.country_id}"
    
class country:
    def __init__(self, country_id, country):
        self.country_id = country_id
        self.country = country
    def showobject(self):
        return f"{self.country_id}, {self.country}"
    
class password:
    def __init__(self, password_id, password):
        self.password_id = password_id
        self.password = password
    def showobject(self):
        return f"{self.password_id}, {self.password}"
    
class location:
    def __init__(self, location_id, zip, location):
        self.location_id = location_id
        self.zip = zip
        self.location = location
    def showobject(self):
        return f"{self.location_id}, {self.zip}, {self.location}"
    
class vendor:
    def __init__(self, vendor_id, name, street, houseNumber, email, ort_id, laender_id, password_id):
        self.vendor_id = vendor_id
        self.name = name
        self.street = street
        self.houseNumber = houseNumber
        self.email = email
        self.ort_id = ort_id
        self.laender_id = laender_id
        self.password_id = password_id

    def showObject(self):
        return f"{self.vendor_id}, {self.name}, {self.street}, {self.houseNumber}, {self.email}, {self.ort_id}, {self.laender_id}, {self.password_id}"


class customer(vendor):
    def __init__(self, vendor_id, name, street, houseNumber, email, ort_id, laender_id, password_id, forename, birthday):
        super().__init__(vendor_id, name, street, houseNumber, email, ort_id, laender_id, password_id)
        self.customer_id = vendor_id  # kunde_id ist nur ein Alias für vendor_id
        self.forename = forename
        self.birthday = birthday

    def showObject(self):
        return f"{self.customer_id}, {self.forename}, {self.birthday}, {self.name}, {self.street}, {self.houseNumber}, {self.email}, {self.ort_id}, {self.laender_id}, {self.password_id}"


    
