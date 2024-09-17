from flask import Flask
import mysql.connector
import numpy as np 

app = Flask(__name__, static_url_path='', static_folder='static')

def db_connect():
    return mysql.connector.connect(        
        host="172.16.182.142",
        user="power_user",
        password="adrian_stinkt",
        database="shopsystem"
    )

def get_produkte():
    conn = db_connect()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM Produkte"

    cursor.execute(query)

    result = cursor.fetchall()
    return result


products = get_produkte()



class product:
    def __init__(self, product_id, product_name, preis, hersteller_id):
        self.product_id = product_id
        self.product_name = product_name
        self.preis = preis
        self.hersteller_id = hersteller_id
    def showobject(self):
        return f"{self.product_id}, {self.product_name}"


product_objects = {}
for n in products:
    obj = product(n['produkt_id'], n['produkt_name'], n['preis'], n['hersteller_id'])    
    product_objects[n['produkt_name']] = obj

print(product_objects)

if __name__ == '__main__':
    app.run(debug=True)

