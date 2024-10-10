from functions import db_connect


#Function to edit a product using the id, possible to change the name and price
def edit_product(product_id, product_name = None, price = None):
    if product_name is not None or isinstance(product_name, str):
        raise ValueError("Product name must be a string!")
    conn = db_connect()
    cursor = conn.cursor(dictionary=True)
    #dynamic array to only change given arguments
    fields = []
    values = []

    #add %s to fields
    if product_name:
        fields.append("produkt_name= %s")
        values.append(product_name)

    if price is not None:
        fields.append("price = %s")
        values.append(price)

    if not fields:
        print("Keine Änderungen")
        return
    
    query = "UPDATE product SET " + ", " .join(fields) + " WHERE produkt_id = %s"
    
    #add product id to use
    values.append(product_id)
    cursor.execute(query, values)
    conn.commit() 
    conn.close()
    return(f"Changed {product_id}")


def edit_customer():
    ""

def edit_vendor():
    ""
