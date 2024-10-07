from functions import db_connect

def get_object_by_id(table_name, object_id):
    conn = db_connect()
    cursor = conn.cursor(dictionary=True)
    query = f"SELECT * FROM {table_name} WHERE id = %s"
    cursor.execute(query, (object_id,))
    result = cursor.fetchone()
    conn.close()
    return result

#returns a list of dictionarys.
#every dictionary is a row of the table.
def get_all_objects(table_name):
    conn = db_connect()
    cursor = conn.cursor(dictionary=True)
    query = f"SELECT * FROM {table_name}"
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result
