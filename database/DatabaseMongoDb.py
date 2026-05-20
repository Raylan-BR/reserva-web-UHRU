from pymongo import MongoClient
from configs.config import Config
from datetime import datetime


class DatabaseMongoDb:
    def __init__(self):
        uri = Config.uri
        client = MongoClient(uri)
        __reservedb = client['reservedb']
        self.__users = __reservedb['users']
        self.__registers = __reservedb['registers']
        self.__registers.create_index(
            "dateTimeEnd",
            expireAfterSeconds=0
        )

    def validate_email(self, _email):
        try:
            response = self.__users.find_one({"email": _email})
            if response:
                return response['name']
        except Exception as e:
            print(f'Error in validate_email method: {e}')
        return None

    def create_user(self, _name, _email):
        try:
            query = {
                'name': _name, 'email': _email
            }
            self.__users.insert_one(query)
            return True
        except Exception as e:
            print(f'Error in create_user method: {e}')
            return False

    def create_register(
            self, _name, _dateTimeStart: datetime, _dateTimeEnd: datetime
        ):
        try:
            query = {
                'name': _name, 'dateTimeStart': _dateTimeStart,
                'dateTimeEnd': _dateTimeEnd
            }
            self.__registers.insert_one(query)
            return True
        except Exception as e:
            print(f'Error in create_register method: {e}')
            return False
    def get_all_register(self, name={}):
        try:
            allReserve = list(self.__registers.find(name))
            for reserve in allReserve:
                reserve['_id'] = str(reserve['_id'])
            return allReserve
        except Exception as e:
            print(f'Error in get_register_all method: {e}')
            return None
    def exist_reserve(
        self, _dateTimeStart: datetime, _dateTimeEnd: datetime
    ):
        # Sobreposição de horários
        return self.__registers.find_one({
            "dateTimeStart": { "$lt": _dateTimeEnd },
            "dateTimeEnd": { "$gt": _dateTimeStart }
        })

db = DatabaseMongoDb()