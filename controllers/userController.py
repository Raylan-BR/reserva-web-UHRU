from flask import request, jsonify, render_template
from models.userModel import userModel

class userController:

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