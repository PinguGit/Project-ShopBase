from flask import Flask
from flask_cors import CORS

# Importiere die beiden Blueprints
from getController import get_blueprint
from pwdController import pwd_blueprint

app = Flask(__name__)
CORS(app)

# Registriere die Blueprints
app.register_blueprint(get_blueprint, url_prefix='/api')
app.register_blueprint(pwd_blueprint, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
