from flask import Blueprint
from controllers.authController import authController

auth = Blueprint('auth', __name__)

auth.route('/login', methods=['POST'])(
    authController.login
)