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

def edit_product(product_id, product_name = None, price = None):
    conn = db_connect()
    cursor = conn.cursor(dictionary=True)

    fields = []
    values = []
    if product_name:
        fields.append("produkt_name= %s")
        values.append(product_name)

    if price is not None:
        fields.append("price = %s")
        values.append(price)

    if not fields:
        print("Keine Änderungen")
        return
    
    query = "UPDATE produkte SET " + ", " .join(fields) + "WHERE produkt_id = %s"
    values.append(product_id)
    cursor.execute(query, values)
    result = cursor.fetchall()
    return result


def get_produkte():
    conn = db_connect()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM Produkte"
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def get_hersteller():
    ""

def get_kunden():
    ""

def get_verkaeufer():
    ""