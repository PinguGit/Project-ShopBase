from flask import Flask
import mysql.connector
from Backend.db_get import get_Country_by_Id, getCountryById, getLocationById, getManufacturerById
import classes
from functions import db_connect

def getProducts(listOfDictionarys):
    products_dict = {}
    for row in listOfDictionarys:
        manufacturer_info = getManufacturerById(row['hersteller_id'])
        product_id = row['produkt_id']
    
        products_dict[product_id] = {
            'produkt_name': row['produkt_name'],
            'preis': row['preis'],
            'hersteller': manufacturer_info['hersteller_name'] if manufacturer_info else None,
            'herstellerland': getCountryById(manufacturer_info['laender_id']) if manufacturer_info else None
        }
    return products_dict

def getCustomers(listOfDictionarys):
    customers_dict = {}
    for row in listOfDictionarys:
        customer_id = row['kunden_id']
        location_info = getLocationById(row['ort_id'])
        country_name = getCountryById(row['laender_id'])
        
        customers_dict[customer_id] = {
            'vorname': row['vorname'],
            'nachname': row['nachname'],
            'strasse': row['strasse'],
            'hausnummer': row['hausnummer'],
            'email': row['email'],
            'ort': location_info['ort_name'] if location_info else None,
            'plz': location_info['plz'] if location_info else None,
            'land': country_name if country_name else None
        }
    return customers_dict

def getManufacturers(listOfDictionarys):
    manufacturers_dict = {}
    for row in listOfDictionarys:
        country_name = getCountryById(row['laender_id'])
        manufacturer_id = row['hersteller_id']

        manufacturers_dict[manufacturer_id] = {
            'hersteller_name': row['hersteller_name'],
            'land': country_name if country_name else None
        }
    return manufacturers_dict