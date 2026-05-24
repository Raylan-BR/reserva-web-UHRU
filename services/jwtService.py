import jwt
from configs.config import Config
from datetime import datetime, timedelta, timezone
from flask import request

class jwtService:
    @staticmethod
    def generateToken(name):
        payload = {
            'name': name,
            'exp': datetime.now(timezone.utc) + timedelta(hours=1)
        }
        return jwt.encode(payload, Config.jwt_secret, algorithm='HS256')
    
    @staticmethod
    def validateToken(token):
        try:
            return jwt.decode(token, Config.jwt_secret, algorithms=['HS256'])
        except:
            return None
    
    @staticmethod
    def getTokenRequest():
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return {'error': 'Token not send'}
        try:
            return auth_header.split(' ')[1]
        except:
            return {'error': 'Invalid format'}