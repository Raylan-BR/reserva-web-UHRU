from functools import wraps
from services.jwtService import jwtService
from flask import jsonify
from configs.config import Config

def checkToken(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = jwtService.getTokenRequest()

        if isinstance(token, dict):
            return jsonify(token), 200
        
        payload = jwtService.validateToken(token)
        
        if not payload:
            return jsonify({'error': 'Invalid token'}), 200
        return f(*args, **kwargs)
    return decorator

def checkAdm(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = jwtService.getTokenRequest()

        if isinstance(token, dict):
            return jsonify(token), 200
        
        if not token == Config.token_adm:
            return jsonify({'error': 'Invalid token'}), 200
        return f(*args, **kwargs)
    return decorator
        
