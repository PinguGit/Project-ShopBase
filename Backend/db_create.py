from functions import db_connect
from flask import Flask
import bcrypt

def create_product(product_name, price):
    conn = db_connect()
    cursor = conn.cursor(dictionary=True)

    query = "INSERT INTO produkte table ('produkt_name', 'preis') VALUES (%s, %s))"

    cursor.execute(query, (product_name, price))
    result = cursor.fetchall

    conn.close()
    return result

# create a new user
def register_user(forename, lastname, street, housenumber, email, password, location_id, location, laender_id, isCustomer, birthdate):
    
    # password hashing
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    # get primarykey of location and insert new location
    location_primary = get_or_create_location(location_id, location)
    
    conn = db_connect()
    cursor = conn.cursor()

    try:
        # save the password
        cursor.execute("INSERT INTO passwort (password) VALUES (%s)", (hashed_password.decode('utf-8'),))
        password_id = cursor.lastrowid

        if isCustomer == 'private':
            # save customer data
            cursor.execute("""
                INSERT INTO kunde (vorname, nachname, strasse, hausnummer, email, ort_id, laender_id, password_id, geburtsdatum) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, (forename, lastname, street, housenumber, email, location_primary, laender_id, password_id, birthdate))
        else:
            # save vendor data
            cursor.execute("""
                INSERT INTO verkaeufer (name, strasse, hausnummer, email, ort_id, laender_id, password_id) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, (forename, street, housenumber, email, location_primary, laender_id, password_id)) 

        conn.commit()

        return True

    except Exception as e:
        conn.rollback()
        return (f"Fehler bei der Registrierung: {str(e)}")
    
    finally:
        conn.close()

# user login
def login_user(email, entered_password, isCustomer):

    conn = db_connect()
    cursor = conn.cursor(dictionary=True)

    if isCustomer == 'private':
    # get user data if customer
        query = """
            SELECT k.kunden_id, p.password 
            FROM kunde k 
            JOIN passwort p ON k.password_id = p.password_id 
            WHERE k.email = %s
        """
    else:
        query = """
            SELECT v.verkaeufer_id, p.password
            FROM verkaeufer v 
            JOIN passwort p ON v.password_id = p.password_id 
            WHERE v.email = %s
        """
    cursor.execute(query, (email,))
    result = cursor.fetchone()
    conn.close()

    # check if user exists
    if not result:
        print("Benutzer nicht gefunden.")
        return False

    stored_hashed_password = result['password']

    # verify password
    if bcrypt.checkpw(entered_password.encode('utf-8'), stored_hashed_password.encode('utf-8')):
        print("Login erfolgreich!")
        return result
    else:
        print("Falsches Passwort.")
        return False

def get_or_create_location(location_id, location):
    conn = db_connect()
    cursor = conn.cursor(dictionary=True)

    # check if location_id exists
    query = "SELECT ort_id FROM orte WHERE plz = %s"
    cursor.execute(query, (location_id,))
    result = cursor.fetchone()

    # return id
    if result:
        conn.close()
        return result['ort_id']

    # else insert data
    insert_query = "INSERT INTO orte (plz, ort_name) VALUES (%s, %s)"
    cursor.execute(insert_query, (location_id, location))
    conn.commit()

    # get new id
    new_ort_id = cursor.lastrowid
    conn.close()

    return new_ort_id
