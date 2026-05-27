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
        try:
            __token = auth_header.split(' ')[1]
            if not auth_header:
                return {
                    'sucess': False,
                    'message': 'TOKEN_NOT_SEND'}
            return __token
        except:
            return {
                'sucess': False,
                'message': 'FORMAT_TOKEN_INVALID'}
        
    @staticmethod
    def getNameForToken(token):
        try:
            if not isinstance(token, str):
                return None
            payload = jwtService.validateToken(token)
            return payload['name']
        except:
            print('User not token !')
            return None