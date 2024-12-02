from flask import Flask, jsonify, request, Blueprint
from flask_cors import CORS
from db_create import create_bestellungen

# Flask App Setup
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

# Blueprint Setup
create_blueprint = Blueprint('create_blueprint', __name__)

@create_blueprint.route('/create_bestellung/<kunden_id>', methods=['POST', 'OPTIONS'])
def createBestellung(kunden_id):
    # OPTIONS Handler für CORS Preflight-Anfrage
    if request.method == 'OPTIONS':
        response = jsonify({'message': 'CORS Preflight erfolgreich'})
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Methods', 'POST, OPTIONS')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        return response, 204

    # POST-Anfrage zur Erstellung einer Bestellung
    try:
        # JSON-Daten validieren
        data = request.get_json()
        if not data or 'products' not in data:
            return jsonify({'error': 'Ungültige Anfrage. "products" ist erforderlich.'}), 400

        # Produkte aus der Anfrage extrahieren
        products = data['products']
        if not isinstance(products, list) or len(products) == 0:
            return jsonify({'error': 'Keine Produkte übermittelt oder falsches Format'}), 400

        # Bestellung erstellen
        create_bestellungen(kunden_id, products)
        return jsonify({'success': True, 'message': 'Bestellung erfolgreich erstellt'}), 201

    except Exception as e:
        # Fehlerbehandlung mit vollständiger Ausgabe für Debugging
        return jsonify({'error': f'Fehler bei der Bestellung: {str(e)}'}), 500

# Blueprint registrieren
app.register_blueprint(create_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
