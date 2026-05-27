from database.DatabaseMongoDb import db
from models.reserveModel import reserveModel
import re

class userModel(reserveModel):
    @staticmethod
    def validateUserForEmail(email):
        if not userModel.__checkEmail(email):
            return {
                'sucess': False,
                'message': 'INVALID_EMAIL'}
        name = db.validate_email(email)
        if not name:
            return {
                'sucess': False,
                'message': 'NOT_FOUND_EMAIL'}
        return {
            'sucess': True,
            'name': name}
    @staticmethod
    def __checkEmail(email):
        __email = r'^[a-zA-Z0-9._%+-]+@discente\.ufma\.br$'
        if re.fullmatch(__email, email):
            return True
        else:
            return False