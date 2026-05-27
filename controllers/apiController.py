from flask import request, jsonify
from models.userModel import userModel
from services.jwtService import jwtService

class apiController:
    @staticmethod
    def getTokenLogin():
        try:
            datas = request.json
            userEmail = datas.get('email')
            status = userModel.validateUserForEmail(userEmail)
            if status['sucess']:
                token = jwtService.generateToken(status['name'])
                if not token:
                    return jsonify({
                            'sucess': False,
                            'message': 'NOT_GENERATE_TOKEN'
                        }), 401
                return jsonify({
                            'sucess': True,
                            'token': token}), 200
            else:
                return jsonify(status), 401
        except:
            print('Error in getTokenLogin method !')
            return jsonify({
                            'sucess': False,
                            'message': 'PROBLEMS_IN_PROCESS'
                        }), 401
        
    @staticmethod
    def getMyAllReserve():
        myAllReserve = userModel.getMyAllReserve()
        if not myAllReserve:
            return jsonify([]), 200
        return jsonify(myAllReserve), 200
    
    @staticmethod
    def setMyReserve():
        try:
            datas = request.json
            dateTimeStart = datas.get('dateTimeStart')
            dateTimeEnd = datas.get('dateTimeEnd')

            return jsonify(
                userModel.createReserve(dateTimeStart, dateTimeEnd))
        except:
            print('Error in setMyReserve method !')
            jsonify({
                    'sucess': False,
                    'message': 'INVALID_DATES'
                        }), 400

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