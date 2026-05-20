from database.DatabaseMongoDb import db
from models.reserveModel import reserveModel
import re

class userModel(reserveModel):
    @staticmethod
    def validateUserForEmail(email):
        if not userModel.__checkEmail(email):
            return {'error': 'Invalid email'}
        name = db.validate_email(email)
        if not name:
            return {'error': 'Not found email'}
        return {'name': name}
    @staticmethod
    def __checkEmail(email):
        __email = r'^[a-zA-Z0-9._%+-]+@discente\.ufma\.br$'
        if re.fullmatch(__email, email):
            return True
        else:
            return False