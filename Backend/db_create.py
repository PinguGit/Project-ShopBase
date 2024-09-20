from functions import db_connect
from flask import Flask

def create_user(user_type, user_id, name, street, houseNumber, email, ort_id, laender_id, password_id, forename=None, birthday=None):
    conn = db_connect()
    cursor = conn.cursor()

    if user_type == "vendor":
        # SQL Query to insert into the vendor table
        query = """
            INSERT INTO vendor (verkauefer_id, name, strasse, hausnummer, email, ort_id, laender_id, password_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (user_id, name, street, houseNumber, email, ort_id, laender_id, password_id))

    elif user_type == "customer":
        # SQL Query to insert into the customer table
        query = """
            INSERT INTO customer (kunden_id, vorname, nachname, strasse, hausnummer, email, ort_id, laender_id, password_id, geburtsdatum,)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (user_id, forename, birthday, name, street, houseNumber, email, ort_id, laender_id, password_id))

    else:
        raise ValueError("Invalid user_type. Must be 'vendor' or 'customer'.")

    conn.commit()  
    conn.close()

def create_product(product_name, price):
    conn = db_connect()
    cursor = conn.cursor(dictionary=True)
    query = "INSERT INTO produkte table ('produkt_name', 'preis') VALUES (%s, %s))"
    cursor.execute(query, (product_name, price))
    result = cursor.fetchall
    conn.close()
    return result