from classes import order
from functions import db_connect

def getObjectById(table_name, object_id):
    conn = db_connect()
    cursor = conn.cursor(dictionary=True)
    query = f"SELECT * FROM {table_name} WHERE id = %s"
    cursor.execute(query, (object_id,))
    result = cursor.fetchone()
    conn.close()
    return result

def getCountryById(laender_id):
    conn = db_connect()
    cursor = conn.cursor(dictionary=True)  
    query = "SELECT land FROM laender WHERE laender_id = %s"
    cursor.execute(query, (laender_id,))
    result = cursor.fetchone()
    conn.close()
    return result['land'] if result else None

#returns a list of dictionarys.
#every dictionary is a row of the table.
def getAllObjects(table_name):
    conn = db_connect()
    cursor = conn.cursor(dictionary=True)
    query = f"SELECT * FROM {table_name}"
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result

#get all orders of a customer
def getCustomerOrders(kunden_id):
    conn = db_connect() 
    cursor = conn.cursor(dictionary=True)
    
    query = """
    SELECT 
        b.bestell_id,
        b.anzahl,
        b.gesamtpreis,
        p.produkt_name,
        p.preis AS einzelpreis,
        h.hersteller_name
    FROM 
        kundenbestellungen kb
    JOIN 
        bestellung b ON kb.bestell_id = b.bestell_id
    JOIN 
        verkaeufer_produkte vp ON b.verkaeufer_produkt_id = vp.verkaeufer_produkt_id
    JOIN 
        product p ON vp.produkt_id = p.produkt_id
    JOIN 
        hersteller h ON p.hersteller_id = h.hersteller_id
    WHERE 
        kb.kunden_id = %s
    """
    
    cursor.execute(query, (kunden_id,))
    result = cursor.fetchall()
    conn.close()
    
 # Create a list of order dictionarys
    orders_dict = {}
    for row in result:
        order_id = row['bestell_id']
        orders_dict[order_id] = {
            'anzahl': row['anzahl'],
            'gesamtpreis': row['gesamtpreis'],
            'produkt_name': row['produkt_name'],
            'einzelpreis': row['einzelpreis'],
            'hersteller_name': row['hersteller_name']
        }
    
    return orders_dict

def getLocationById(ort_id):
    conn = db_connect()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT plz, ort_name FROM orte WHERE ort_id = %s"
    cursor.execute(query, (ort_id,))
    result = cursor.fetchone()
    conn.close()
    return result if result else None

def getManufacturerById(manufacturerId):
    conn = db_connect()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT hersteller_name, laender_id FROM hersteller WHERE hersteller_id = %s"
    cursor.execute(query, (manufacturerId,))
    result = cursor.fetchone()
    conn.close()
    return result if result else None

