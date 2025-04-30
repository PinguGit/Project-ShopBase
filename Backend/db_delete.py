from functions import db_connect


def delete_by_obejct(obj):
    obj_type = type(obj).__name__
    #Case Statements to get the correct table and id by the class
    match obj_type:
        case "product":
            table = "product"
            column = "produkt_id"
            id = obj.product_id
        case "manufacturer":
            table = "hersteller"
            column = "hersteller_id"
            id = obj.manufacturer_id
        case "country":
            table = "laender"
            column = "laender_id"
            id = obj.country_id
        case "password":
            table = "passwort"
            column = "password_id"
            id = obj.password_id
        case "location":
            table = "orte"
            column = "location_id"
            id = obj.location_id
        case "vendor":
            table = "verkauefer"
            column = "verkauefer_id"
            id = obj.vendor_id
        case "customer":
            table = "kunde"
            column = "kunden_id"
            id = obj.customer_id


    conn = db_connect()
    cursor = conn.cursor(dictionary=True)

    #try to excecute the query    
    try:
        query = f"DELETE FROM {table} WHERE {column} = {id}"
        cursor.execute(query)
        conn.commit()
        print(f"Exceuted Delete Statement: {query}")

    #if failure do a rollback to ensure no destroying of the database
    except Exception as error:
        conn.rollback()
        print(f"Failure by committing query {error}")
    finally:
        cursor.close()
        conn.close()
    
