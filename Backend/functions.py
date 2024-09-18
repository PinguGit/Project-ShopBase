from flask import Flask
import mysql.connector


def db_connect():
    return mysql.connector.connect(        
        host="172.16.182.142",
        user="power_user",
        password="adrian_stinkt",
        database="shopsystem"
    )

def create_product(product_name, ):
    conn = db_connect()
    cursor = conn.cursor(dictionary=True)
    query = "INSERT INTO produkte table ('produkt_name', 'preis') VALUES '{}')"


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