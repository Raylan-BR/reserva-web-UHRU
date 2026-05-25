from flask import Blueprint
from controllers.apiController import apiController
from middlewares.checkToken import checkToken

api = Blueprint('api', __name__)

api.route('/api/getTokenLogin', methods=['POST'])(
    apiController.getTokenLogin
)
api.route('/api/getMyAllReserve', methods=['GET'])(
    checkToken(apiController.getMyAllReserve)
)
api.route('/api/setMyReserve', methods=['POST'])(
    checkToken(apiController.setMyReserve)
)
api.route('/api/delete/<id>', methods=['DELETE'])(
    checkToken(apiController.deleteReserve)
)
api.route('/api/getAllReserve', methods=['GET'])(
    apiController.getAllReserve
)