import datetime
import mysql
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

    conn = db_connect()
    cursor = conn.cursor()

    # get primarykey of location and insert new location
    # check if location_id exists
    query = "SELECT ort_id FROM orte WHERE plz = %s"
    cursor.execute(query, (location_id,))
    result = cursor.fetchone()

    # return id
    if result:
         location_primary = result[0]
    # create a new location
    else:
        insert_query = "INSERT INTO orte (plz, ort_name) VALUES (%s, %s)"
        cursor.execute(insert_query, (location_id, location))
        location_primary = cursor.lastrowid

    try:
        # save the password
        cursor.execute("INSERT INTO passwort (password) VALUES (%s)", (hashed_password.decode('utf-8'),))
        password_id = cursor.lastrowid

        if isCustomer == 'private':
            cursor.execute("SELECT kunden_id FROM kunde WHERE email = %s", (email,))
            existing_user = cursor.fetchone()

            if existing_user:
                return {'error': 'Email already exists'}
            
            if None in (forename, lastname, street, housenumber, email, location_primary, laender_id, password_id, birthdate):
                return 'Fehler: Einer der Werte ist None'
            # save customer data
            cursor.execute("""
                INSERT INTO kunde (vorname, nachname, strasse, hausnummer, email, ort_id, laender_id, password_id, geburtsdatum) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (forename, lastname, street, housenumber, email, location_primary, laender_id, password_id, birthdate))

            # get the ID of the newly created row
            customer_id = cursor.lastrowid
            conn.commit()
            # return the ID of the created customer
            return {'success': True, 'kunden_id': customer_id}
        
        else:
            cursor.execute("SELECT verkaeufer_id FROM verkaeufer WHERE email = %s", (email,))
            existing_user = cursor.fetchone()

            if existing_user:
                return {'error': 'Email already exists'}
            
            # save vendor data
            cursor.execute("""
                INSERT INTO verkaeufer (name, strasse, hausnummer, email, ort_id, laender_id, password_id) 
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (forename, street, housenumber, email, location_primary, laender_id, password_id)) 

            # get the ID of the newly created row
            vendor_id = cursor.lastrowid
            conn.commit()
            # return the ID of the created vendor
            return {'success': True, 'verkaeufer_id': vendor_id}

    except Exception as e:
        conn.rollback()
        return (f"Fehler bei der Registrierung: {str(e)}")
    
    finally:
        cursor.close()
        conn.close()

# user login
def login_user(email, entered_password, isCustomer):
   
    conn = db_connect()
    cursor = conn.cursor(dictionary=True)
    print(isCustomer, email)
    if isCustomer == 'private':
    # get user data if customer
        query = """
            SELECT k.kunden_id AS id, p.password 
            FROM kunde k 
            JOIN passwort p ON k.password_id = p.password_id 
            WHERE k.email = %s
        """
    elif isCustomer == 'business':
        query = """
            SELECT v.verkaeufer_id AS id, p.password
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
        if isCustomer == 'private' and 'kunden_id' in result:
            print("Login successful as customer.")
            return result  # Return the customer data
        elif isCustomer == 'business' and 'verkaeufer_id' in result:
            print("Login successful as vendor.")
            return result  # Return the vendor data
        else:
            print("Login failed: mismatched user type.")
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

def create_bestellungen(kunden_id, products):
    conn = db_connect()
    cursor = conn.cursor(dictionary=True)
    
    try:
        bestell_ids = []
        
        for product in products:
            produkt_id = product['produkt_id']  # Erwarte produkt_id statt verkaeufer_produkt_id
            anzahl = product['anzahl']
            gesamtpreis = product['gesamtpreis']
            
            # `verkaeufer_produkt_id` basierend auf `produkt_id` abrufen
            cursor.execute("""
                SELECT verkaeufer_produkt_id FROM verkaeufer_produkte WHERE produkt_id = %s
            """, (produkt_id,))
            result = cursor.fetchone()
            
            if result:
                verkaeufer_produkt_id = result[0]
                
                # Eintrag in die Tabelle `bestellung`
                cursor.execute("""
                    INSERT INTO bestellung (verkaufer_produkt_id, anzahl, gesamtpreis)
                    VALUES (%s, %s, %s)
                """, (verkaeufer_produkt_id, anzahl, gesamtpreis))
                
                # get bestell_id for new kundenbestellungen
                bestell_id = cursor.lastrowid
                bestell_ids.append(bestell_id)
                
                # create entry in kundenbestellungen
                cursor.execute("""
                    INSERT INTO kundenbestellungen (kunden_id, bestell_id)
                    VALUES (%s, %s)
                """, (kunden_id, bestell_id))
            else:
                # if no produkt_id was found
                raise ValueError(f"Produkt-ID {produkt_id} nicht in verkaeufer_produkte gefunden.")
        
        # complete transaktion
        conn.commit()
        return {'success': True, 'bestell_ids': bestell_ids}

    # undo changes
    except (mysql.connector.Error, ValueError) as err:
        conn.rollback()
        return {'success': False, 'error': str(err)}

    finally:
        cursor.close()
        conn.close()


def save_session_token(email, token):

    conn = db_connect()
    cursor = conn.cursor(dictionary=True)
    
    expiration = datetime.now() + datetime.timedelta(hours=1)
    
    cursor.execute(
        """
        INSERT INTO sessions (email, token, expiration) 
        VALUES (%s, %s, %s)
        ON DUPLICATE KEY UPDATE token = %s, expiration = %s
        """,
        (email, token, expiration, token, expiration)
    )
    conn.commit()
    conn.close()
