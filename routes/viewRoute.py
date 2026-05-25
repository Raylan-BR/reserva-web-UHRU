from flask import Blueprint
from controllers.viewController import viewController

view = Blueprint('view', __name__)

view.route('/', methods=['GET'])(
    viewController.getHomePage
)
view.route('/nav', methods=['GET'])(
    viewController.getNavPage
)
view.route('/login', methods=['GET'])(
    viewController.getLoginPage
)
view.route('/getAllReserve', methods=['GET'])(
    viewController.getAllReserve
)