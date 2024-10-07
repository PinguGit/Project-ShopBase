from flask import Flask
import mysql.connector
import classes
from functions import db_connect

def getProducts(listOfDictionarys):
    product_objects = {}
    for n in listOfDictionarys:
        obj_product = classes.product(n['produkt_id'], n['produkt_name'], n['preis'], n['hersteller_id'])    
        product_objects[n['produkt_id']] = obj_product
    return product_objects

def getCustomers(listOfDictionarys):
    customer_objects = {}
    for n in listOfDictionarys:
        obj_customer = classes.product(n['produkt_id'], n['produkt_name'], n['preis'], n['hersteller_id'])    
        customer_objects[n['produkt_id']] = obj_customer
    return customer_objects

def getManufacturers(listOfDictionarys):
    manufacturers_objects = {}
    for n in listOfDictionarys:
        obj_manufacturer = classes.manufacturer(n["hersteller_id"], n["hersteller_name"], n["laender_id"])
        manufacturers_objects[n['hersteller_id']] = obj_manufacturer
    return manufacturers_objects