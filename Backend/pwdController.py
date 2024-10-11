from flask_cors import CORS
from flask import Flask, jsonify, request
import db_create

app = Flask(__name__)
CORS(app)

# returns true or false whether it successfully creates a user
@app.route('/api/registerUser', methods=['POST'])
def registerUser():
    data = request.json
    forename = data.get('forename')
    lastname = data.get('lastname')
    street = data.get('street')
    housenumber = data.get('housenumber')
    email = data.get('email')
    password = data.get('password')
    location_id = data.get('location_id')
    location = data.get('location')
    laender_id = data.get('laender_id')
    birthdate = data.get('birthdate')
    isCustomer = data.get('isCustomer')

    result = db_create.register_user(forename, lastname, street, housenumber, email, password, location_id, location, laender_id, isCustomer, birthdate)
    return jsonify({'success': result})

# returns true or false whether it successfully verifies a user
@app.route('/api/loginUser', methods=['POST'])
def loginUser():
    data = request.json
    email = data.get('email')
    entered_password = data.get('entered_password')
    isCustomer = data.get('isCustomer')

    result = db_create.login_user(email, entered_password, isCustomer)
    return jsonify({'success': result})

if __name__ == '__main__':
    app.run(debug=True)
