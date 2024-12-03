from flask import Flask
from flask_cors import CORS

# Importiere die beiden Blueprints
from Backend.Controller.getController import get_blueprint
from Backend.Controller.pwdController import pwd_blueprint
from Backend.Controller.createController import create_blueprint

app = Flask(__name__)
CORS(app)

# Registriere die Blueprints
app.register_blueprint(get_blueprint, url_prefix='/api')
app.register_blueprint(pwd_blueprint, url_prefix='/api')
app.register_blueprint(create_blueprint, url_prefix='/api')

from functools import wraps
from flask import request, jsonify

if __name__ == '__main__':
    app.run(debug=True, port=5000)
