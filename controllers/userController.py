from flask import request, jsonify, render_template
from models.userModel import userModel

class userController:

    @staticmethod
    def getMyAllReserve():
        myAllReserve = userModel.getMyAllReserve()
        if not myAllReserve:
            return jsonify({'error': 'Reserves not found'}), 401
        return jsonify({'my_reserve': myAllReserve}), 200
    
    @staticmethod
    def setMyReserve():
        datas = request.json
        dateTimeStart = datas.get('dateTimeStart')
        dateTimeEnd = datas.get('dateTimeEnd')

        return jsonify(
            userModel.createReserve(dateTimeStart, dateTimeEnd))

    @staticmethod
    def getAllReserve():
        allReserve = userModel.getAllReserve()
        if not allReserve:
            return jsonify({'error': 'Reserves not found'}), 401
        return jsonify({'all_reserve': allReserve}), 200