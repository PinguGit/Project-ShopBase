from flask import Flask
import mysql.connector


def db_connect():
    return mysql.connector.connect(        
        host="172.16.182.142",
        user="power_user",
        password="adrian_stinkt",
        database="shopsystem"
    )

def create_product(product_name, price):
    conn = db_connect()
    cursor = conn.cursor(dictionary=True)
    query = "INSERT INTO produkte table ('produkt_name', 'preis') VALUES (%s, %s))"
    cursor.execute(query, (product_name, price))
    result = cursor.fetchall
    conn.close
    return result


#Function to edit a product using the id, possible to change the name and price
def edit_product(product_id, product_name = None, price = None):
    if product_name is not None or isinstance(product_name, str):
        raise ValueError("Product name must be a string!")
    conn = db_connect()
    cursor = conn.cursor(dictionary=True)
    #dynamic array to only change given arguments
    fields = []
    values = []

    #add %s to fields
    if product_name:
        fields.append("produkt_name= %s")
        values.append(product_name)

    if price is not None:
        fields.append("price = %s")
        values.append(price)

    if not fields:
        print("Keine Änderungen")
        return
    
    query = "UPDATE product SET " + ", " .join(fields) + " WHERE produkt_id = %s"
    
    #add product id to use
    values.append(product_id)
    cursor.execute(query, values)
    conn.commit() 
    return(f"Changed {product_id}")

def delete_by_obejct(obj):
    print(obj.type)

    


def get_product():
    conn = db_connect()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM product"
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def get_manufacturer():
    conn = db_connect()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM manufacturer"
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def get_customer():
    conn = db_connect()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM kunde"
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def get_vendor():
    conn = db_connect()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM vendor"
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def edit_customer():
    ""

def edit_vendor():
    ""

def delete():
    ""

