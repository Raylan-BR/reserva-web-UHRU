from flask import Blueprint
from controllers.viewController import viewController
from middlewares.checkToken import checkToken

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
view.route('/item', methods=['GET'])(
    viewController.getItemPage
)
view.route('/form', methods=['GET'])(
    viewController.getFormReservePage
)
view.route('/myItem', methods=['GET'])(
   checkToken(viewController.getItemPageWithDelete)
)