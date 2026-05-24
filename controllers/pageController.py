from flask import render_template
from services.jwtService import jwtService

class pageController:
    @staticmethod
    def getHome():
        return render_template('index.html')

    @staticmethod
    def getNav():
        __name = jwtService.getNameForToken(
            jwtService.getTokenRequest()
        )
        return render_template(
            'include/nav.html',
            user_name=__name)