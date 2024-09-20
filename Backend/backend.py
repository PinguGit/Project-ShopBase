from flask import Flask
import mysql.connector
import classes
import functions
<<<<<<< HEAD
import db_get
import db_delete
=======
import db_delete

>>>>>>> 94db405 (Update Backend.py)

app = Flask(__name__, static_url_path='', static_folder='static')

db_get.get_product

products = db_get.get_product()
product_objects = {}

for n in products:
    obj_products = classes.product(n['produkt_id'], n['produkt_name'], n['preis'], n['hersteller_id'])    
    product_objects[n['produkt_id']] = obj_products

manufactures = functions.get_manufacturer
manufactures_objects_dic = {}

for n in manufactures_objects_dic:
    obj_manufactures = classes.manufacturer(n["hersteller_id"], n["hersteller_name"], n["laender_id"])
    manufactures_objects_dic[n]

print(product_objects)





print(db_delete.delete_by_obejct(product_objects.get("Wasser")))

if __name__ == '__main__':
    app.run(debug=True)

