from flask import Blueprint
from controllers.userController import userController
from middlewares.authMiddleware import checkToken

user = Blueprint('user', __name__)

user.route('/getMyAllReserve', methods=['GET'])(
    checkToken(userController.getMyAllReserve)
)
user.route('/setMyReserve', methods=['POST'])(
    checkToken(userController.setMyReserve)
)
user.route('/delete/<id>', methods=['DELETE'])(
    checkToken(userController.deleteReserve)
)
user.route('/getAllReserve', methods=['GET'])(
    userController.getAllReserve
)
user.route('/', methods=['GET'])(
    userController.getHomePage
)