from functions import db_connect

def get_product():
    conn = db_connect()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM product"
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result

def get_manufacturer():
    conn = db_connect()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM hersteller"
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result

def get_customer():
    conn = db_connect()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM kunde"
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result

def get_vendor():
    conn = db_connect()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM vendor"
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result