from Backend.Repository.db_get import getAllObjects, getObjectById
import Repository.db_get as db_get
from flask import Blueprint, Flask, jsonify
import Command.getControllerCommand as getControllerCommand
import Command.getCommand as getCommand
import auth_utils
from flask_cors import CORS
from flask import Flask, jsonify

app = Flask(__name__)
CORS(app)


get_blueprint = Blueprint('get_blueprint', __name__)

#returns a specific object from any table
@get_blueprint.route('/get_object/<table>/<objectId>', methods=['GET'])
def getObject(objectId, table):
    dictionary = db_get.getObjectById(table, objectId)
    return jsonify(dictionary)

#returns all orders of a customer
@get_blueprint.route('/get_orders/<customerId>', methods=['GET'])
@auth_utils.token_required
def getOrdersById(customerId):
    dictionary = db_get.getCustomerOrders(customerId)
    return jsonify(dictionary)

#returns all products of a vendor
@get_blueprint.route('/get_products/<vendorId>', methods=['GET'])
def getVendorProducts(vendorId):
    dictionary = db_get.getVendorProducts(vendorId)
    return jsonify(dictionary)

#returns all orders a vendor has to fulfill
@get_blueprint.route('/get_vendor_orders/<vendorId>', methods=['GET'])
@auth_utils.token_required
def getVendorOrdersById(vendorId):
    dictionary = db_get.getVendorOrders(vendorId)
    return jsonify(dictionary)

#returns all entries from following tables:
    #product, kunde, verkauefer, hersteller
@get_blueprint.route('/get_all_objects/<table>', methods=['GET'])
def getAllObjects(table):
    dictionary = db_get.getAllObjects(table)
    json = getControllerCommand.getType(table, dictionary)
    return jsonify(json)
   
if __name__ == '__main__':
    app.run(debug=True)
