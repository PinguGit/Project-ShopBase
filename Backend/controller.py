from Backend.db_get import get_all_objects, get_object_by_id
from flask import Flask, jsonify
import getCommand
from flask_cors import CORS
from flask import Flask, jsonify

app = Flask(__name__)
CORS(app)

@app.route('/api/get_object/<table>/<objectId>', methods=['GET'])
def getObject(objectId, table):
    dictionary = get_object_by_id(table, objectId)
    object = getType(table, dictionary, 0)
    return jsonify(object)

@app.route('/api/get_all_objects/<table>', methods=['GET'])
def getAllObjects(table):
    list = get_all_objects(table)
    objects = getType(table, list, 1)
    return jsonify(objects)

def getType(table, dictionary, check):
    match table:
        case "product":
            if check == 0:
                return
            return getCommand.getProducts(dictionary)
        case "hersteller":
            if check == 0:
                return
            return getCommand.getManufacturers(dictionary)
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
            if check == 0:
                return
            return getCommand.getCustomers(dictionary)
        case "verkauefer_produkte":
            return
    
if __name__ == '__main__':
    app.run(debug=True)
