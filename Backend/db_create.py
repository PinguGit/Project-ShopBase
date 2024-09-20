from functions import db_connect
from flask import Flask

def create_user(user_type, user_id, name, street, houseNumber, email, zip_code, location_name, country_id, plain_password, forename=None, birthday=None):
    conn = db_connect()
    cursor = conn.cursor()

    # 1. Create password
    password_query = "INSERT INTO passwort (password) VALUES (%s)"
    cursor.execute(password_query, (plain_password,))
    password_id = cursor.lastrowid  # Password-ID

     # 2. Check if location already exists
    location_check_query = "SELECT ort_id FROM location WHERE plz = %s AND ort_name = %s"
    cursor.execute(location_check_query, (zip_code, location_name))
    location_result = cursor.fetchone()

    if location_result:
    # 2.1 Get location
        location_id = location_result[0]  # location_id
    else:
    # 2.2 Create location
        location_query = "INSERT INTO orte (plz, ort_name) VALUES (%s, %s)"
        cursor.execute(location_query, (zip_code, location_name))
        location_id = cursor.lastrowid  # location_id

    if user_type == "vendor":
        # 3. Create vendor
        vendor_query = """
            INSERT INTO verkauefer (verkauefer_id, name, strasse, hausnummer, email, ort_id, laender_id, password_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(vendor_query, (user_id, name, street, houseNumber, email, location_id, country_id, password_id))

    elif user_type == "customer":
        # 4. Create customer
        customer_query = """
            INSERT INTO kunde (kunden_id, vorname, nachname, strasse, hausnummer, email, ort_id, laender_id, password_id, geburtsdatum)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(customer_query, (user_id, forename, name, street, houseNumber, email, location_id, country_id, password_id, birthday))

    else:
        raise ValueError("Invalid user_type. Must be 'vendor' or 'customer'.")

    conn.commit()  # Save changes
    conn.close()

def create_product(product_name, price):
    conn = db_connect()
    cursor = conn.cursor(dictionary=True)
    query = "INSERT INTO produkte table ('produkt_name', 'preis') VALUES (%s, %s))"
    cursor.execute(query, (product_name, price))
    result = cursor.fetchall
    conn.close()
    return result