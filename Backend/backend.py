from flask import Flask
import mysql.connector
import classes
import functions

app = Flask(__name__, static_url_path='', static_folder='static')

functions.get_produkte

products = functions.get_produkte()
product_objects = {}

for n in products:
    obj = classes.product(n['produkt_id'], n['produkt_name'], n['preis'], n['hersteller_id'])    
    product_objects[n['produkt_name']] = obj

print(product_objects)

if __name__ == '__main__':
    app.run(debug=True)

