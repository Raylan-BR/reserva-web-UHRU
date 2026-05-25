from flask import render_template
from services.jwtService import jwtService
from services.reserveService import reserveService
from models.userModel import userModel

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
    def getAllReserve():
        allReserve = userModel.getAllReserve()
        allReserve = reserveService.formatationReserve(allReserve)

        return render_template('include/all_reserve.html', all_reserve=allReserve)