from db_get import get_all_objects, get_object_by_id
import db_get
from flask import Flask, jsonify
import getCommand
from flask_cors import CORS
from flask import Flask, jsonify

app = Flask(__name__)
CORS(app)

@app.route('/api/get_object/<table>/<objectId>', methods=['GET'])
def getObject(objectId, table):
    dictionary = db_get.get_object_by_id(table, objectId)
    return jsonify(dictionary)

@app.route('/api/get_orders/<customerId>', methods=['GET'])
def getOrdersById(customerId):
    dictionary = db_get.get_customer_orders(customerId)
    return jsonify(dictionary)

@app.route('/api/get_all_objects/<table>', methods=['GET'])
def getAllObjects(table):
    list = db_get.get_all_objects(table)
    return jsonify(list)
   
if __name__ == '__main__':
    app.run(debug=True)
