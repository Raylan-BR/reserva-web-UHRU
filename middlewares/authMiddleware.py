from functools import wraps
from services.jwtService import jwtService
from flask import request, jsonify

def checkToken(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = getTokenRequest()

        if isinstance(token, dict):
            return jsonify(token), 200
        
        payload = jwtService.validateToken(token)
        
        if not payload:
            return jsonify({'error': 'Invalid token'}), 200
        return f(*args, **kwargs)
    return decorator

def getTokenRequest():
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return {'error': 'Token not send'}
    try:
        return auth_header.split(' ')[1]
    except:
        return {'error': 'Invalid format'}