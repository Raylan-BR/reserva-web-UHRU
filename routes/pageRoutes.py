from flask import Blueprint
from controllers.pageController import pageController

page = Blueprint('page', __name__)

page.route('/', methods=['GET'])(
    pageController.getHome
)
page.route('/nav', methods=['GET'])(
    pageController.getNav
)