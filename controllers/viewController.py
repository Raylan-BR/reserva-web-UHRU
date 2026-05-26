from flask import render_template
from services.jwtService import jwtService

class viewController:
    @staticmethod
    def getHomePage():
        return render_template('index.html')

    @staticmethod
    def getNavPage():
        __name = jwtService.getNameForToken(
            jwtService.getTokenRequest()
        )
        return render_template(
            'include/nav.html',
            user_name=__name)
    @staticmethod
    def getLoginPage():
        return render_template('login.html')
    
    @staticmethod
    def getItemPage():
        return render_template('components/item.html')
    
    @staticmethod
    def getFormReservePage():
        return render_template('include/formReserve.html')