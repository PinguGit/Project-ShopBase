from flask import Flask
import mysql.connector
import db_get
import classes
from functions import db_connect

def getProducts(listOfDictionarys):
    products_dict = {}
    for row in listOfDictionarys:
        # Herstellerinformationen holen
        manufacturer_info = db_get.getManufacturerById(row['hersteller_id'])
        product_id = row['produkt_id']

        # Verkäuferinformationen holen
        vendor_info_list = db_get.getVendorByProductId(product_id)
        
        # Erstelle eine Liste der Verkäufer
        vendors_list = []
        if vendor_info_list:
            for vendor_info in vendor_info_list:
                vendor_details = {
                    'verkaeufer_id': vendor_info['verkaeufer_id'],
                    'verkaeufer_name': vendor_info['name'] if vendor_info else None
                }
                vendors_list.append(vendor_details)
        
        # Produktinformationen im Dictionary speichern
        products_dict[product_id] = {
            'produkt_name': row['produkt_name'],
            'preis': row['preis'],
            'hersteller': manufacturer_info['hersteller_name'] if manufacturer_info else None,
            'herstellerland': db_get.getCountryById(manufacturer_info['laender_id']) if manufacturer_info else None,
            'verkaeufer': vendors_list
        }
    return products_dict


def getCustomers(listOfDictionarys):
    customers_dict = {}
    for row in listOfDictionarys:
        customer_id = row['kunden_id']
        location_info = db_get.getLocationById(row['ort_id'])
        country_name = db_get.getCountryById(row['laender_id'])
        
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
        country_name = db_get.getCountryById(row['laender_id'])
        manufacturer_id = row['hersteller_id']

        manufacturers_dict[manufacturer_id] = {
            'hersteller_name': row['hersteller_name'],
            'land': country_name if country_name else None
        }
    return manufacturers_dict

def getVendors(listOfDictionarys):
    vendors_dict = {}
    for row in listOfDictionarys:
        vendor_id = row['verkaeufer_id']
        location_info = db_get.getLocationById(row['ort_id'])
        country_name = db_get.getCountryById(row['laender_id'])
        
        vendors_dict[vendor_id] = {
            'name': row['name'],
            'strasse': row['strasse'],
            'hausnummer': row['hausnummer'],
            'email': row['email'],
            'ort': location_info['ort_name'] if location_info else None,
            'plz': location_info['plz'] if location_info else None,
            'land': country_name if country_name else None
        }
    
    return vendors_dict
