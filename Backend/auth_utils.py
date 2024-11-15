from functools import wraps
from flask import request, jsonify
import db_get  # Für die Token-Überprüfung (angepasst an dein Setup)

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'success': False, 'message': 'Token is missing!'}), 403
        if not db_get.verify_session_token(token):
            return jsonify({'success': False, 'message': 'Invalid or expired token!'}), 403
        return f(*args, **kwargs)
    return decorated