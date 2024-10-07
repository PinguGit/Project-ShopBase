from Backend.db_get import get_all_objects, get_object_by_id
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/get_products/<table>/<objectId>', methods=['GET'])
def getObject(objectId, table):
    dictionary = get_object_by_id(table, objectId)
    object = getType(table, dictionary)
    return jsonify(object)

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/api/get_all_products/<table>', methods=['GET'])
def getAllObjects(table):
    list = get_all_objects(table)
    #object = getType(table, dictionary)
    return jsonify(list)

if __name__ == '__main__':
    app.run(debug=True)


def getType(table, dictionary):
    match table:
        case "product":
            return 
        case "hersteller":
            return
        case "laender":
            return
        case "kundenbestellungen":
            return
        case "bestellung":
            return
        case "verkauefer":
            return
        case "passwort":
            return
        case "orte":
            return
        case "kunde":
            return
        case "verkauefer_produkte":
            return
    
    
