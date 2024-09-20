from flask import Flask
import mysql.connector
import classes
import functions
import db_get
import db_delete

app = Flask(__name__, static_url_path='', static_folder='static')

db_get.get_product

products = db_get.get_product()
product_objects = {}

for n in products:
    obj_products = classes.product(n['produkt_id'], n['produkt_name'], n['preis'], n['hersteller_id'])    
    product_objects[n['produkt_id']] = obj_products

manufactures = db_get.get_manufacturer()
manufactures_objects_dic = {}

for n in manufactures:
    obj_manufactures = classes.manufacturer(n["hersteller_id"], n["hersteller_name"], n["laender_id"])
    manufactures_objects_dic[n['hersteller_id']] = obj_manufactures

print(product_objects)


db_delete.delete_by_obejct(manufactures_objects_dic.get(1))

if __name__ == '__main__':
    app.run(debug=True)

