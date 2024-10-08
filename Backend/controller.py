from db_get import getAllObjects, getObjectById
import db_get
from flask import Flask, jsonify
import controllerCommand
import getCommand
from flask_cors import CORS
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/get_object/<table>/<objectId>', methods=['GET'])
def getObject(objectId, table):
    dictionary = db_get.getObjectById(table, objectId)
    return jsonify(dictionary)

@app.route('/api/get_orders/<customerId>', methods=['GET'])
def getOrdersById(customerId):
    dictionary = db_get.getCustomerOrders(customerId)
    return jsonify(dictionary)

@app.route('/api/get_all_objects/<table>', methods=['GET'])
def getAllObjects(table):
    dictionary = db_get.getAllObjects(table)
    json = controllerCommand.getType(table, dictionary, 1)
    return jsonify(json)
   
if __name__ == '__main__':
    app.run(debug=True)
