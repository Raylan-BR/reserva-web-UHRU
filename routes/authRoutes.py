from flask import Blueprint
from controllers.authController import authController
from controllers.pageController import pageController

auth = Blueprint('auth', __name__)

auth.route('/login', methods=['POST'])(
    authController.login
)
auth.route('/login', methods=['GET'])(
    authController.getLogin
)