from flask import request, jsonify
from models.userModel import userModel
from services.jwtService import jwtService

class apiController:
    @staticmethod
    def getTokenLogin():
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
    def getMyAllReserve():
        myAllReserve = userModel.getMyAllReserve()
        if not myAllReserve:
            return jsonify([]), 200
        return jsonify(myAllReserve), 200
    
    @staticmethod
    def setMyReserve():
        datas = request.json
        dateTimeStart = datas.get('dateTimeStart')
        dateTimeEnd = datas.get('dateTimeEnd')

        return jsonify(
            userModel.createReserve(dateTimeStart, dateTimeEnd))

    @staticmethod
    def deleteReserve(id):
        status = userModel.deleteReserve(id)
        return jsonify(status), 200

    @staticmethod
    def getAllReserve():
        allReserve = userModel.getAllReserve()
        if not allReserve:
            return jsonify([]), 200
        return jsonify(allReserve), 200