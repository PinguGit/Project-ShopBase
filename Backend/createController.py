from db_create import create_bestellungen
from db_get import getAllObjects, getObjectById
import db_get
from flask import Blueprint, Flask, jsonify, request
import getControllerCommand
import getCommand
from flask_cors import CORS
from flask import Flask, jsonify

app = Flask(__name__)
CORS(app)


create_blueprint = Blueprint('create_blueprint', __name__)

#returns a specific object from any table
@create_blueprint.route('/create_bestellung/<kunden_id>', methods=['POST'])
def createBestellung(kunden_id):
    data = request.get_json()
    products = data.get('products', [])

    if not products:
        return jsonify({'error': 'Keine Produkte übermittelt'}), 400
    
    try:
        create_bestellungen(kunden_id, products)
        return jsonify({'success': True, 'message': 'Bestellung erfolgreich erstellt'}), 201
    except Exception as e:
        return jsonify({'error': f'Fehler bei der Bestellung: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)