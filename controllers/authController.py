from flask import request, jsonify, render_template
from models.userModel import userModel
from services.jwtService import jwtService

class authController:
    @staticmethod
    def login():
        datas = request.json
        userEmail = datas.get('email')
        status = userModel.validateUserForEmail(userEmail)
        try:
            token = jwtService.generateToken(status['name'])
            if not token:
                return jsonify({'error': 'Not generate token'}), 401
            return jsonify({'token': token}), 200
        except Exception as e:
            print(f'Error in login method: {e}')
            return jsonify(status), 401
    @staticmethod
    def getLogin():
        return render_template('login.html')