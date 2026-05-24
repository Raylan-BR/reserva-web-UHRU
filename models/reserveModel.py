from database.DatabaseMongoDb import db
from datetime import datetime, timezone
from zoneinfo import ZoneInfo
from services.jwtService import jwtService
from services.reserveService import reserveService

class reserveModel:  
    @staticmethod
    def createReserve(dateTimeStart, dateTimeEnd):
        __name = reserveModel.getNameForToken(
            jwtService.getTokenRequest()
        )
        __time = reserveModel.validateDateTime(
            dateTimeStart,
            dateTimeEnd
        )
        try:
            db.create_register(
                __name, __time['start'], __time['end'])
            return {'message': 'Sucess create reserve'}
        except Exception as e:
            print(f'Error in createReserve method: {e}')
            return __time
        
    @staticmethod
    def validateDateTime(dateTimeStart, dateTimeEnd):
        try:
            # Conversão de tipo
            _dateTimeStart = datetime.strptime(
                dateTimeStart, "%Y-%m-%d %H:%M"
            ).replace(
                tzinfo=ZoneInfo("America/Sao_Paulo"))
            _dateTimeEnd = datetime.strptime(
                dateTimeEnd, "%Y-%m-%d %H:%M"
            ).replace(
                tzinfo=ZoneInfo("America/Sao_Paulo"))
            
            # Validar dados da requisição
            invalid = reserveService.checkDateTime(
                _dateTimeStart, _dateTimeEnd)
            
            if invalid:
                return invalid    
            
            # Verificar sobreposição de horário
            if reserveModel.__timeOverlap(_dateTimeStart, _dateTimeEnd):
                return {'error': 'Time exist'}

            # Passou pela validação            
            return {'start': _dateTimeStart,
                    'end': _dateTimeEnd}
        
        except Exception as e:
            print(f'Error in __validateDateTime method: {e}')
            return {'error': 'Time convert'}
        
    @staticmethod
    def __timeOverlap(dateTimeStart, dateTimeEnd):
        status = db.exist_reserve(dateTimeStart, dateTimeEnd)
        if status:
            return True
        return False

    @staticmethod
    def getAllReserve():
        allReserve = db.get_all_register()

        return allReserve
    
    @staticmethod
    def getMyAllReserve():
        name = reserveModel.getNameForToken(
            jwtService.getTokenRequest()
        )
        myAllReserve = db.get_all_register({'name': name})
        for myReserve in myAllReserve:
            myReserve["dateTimeStart"] = (
                myReserve["dateTimeStart"]
                .replace(tzinfo=timezone.utc)
                .astimezone(ZoneInfo("America/Sao_Paulo"))
            )
            myReserve["dateTimeEnd"] = (
                myReserve["dateTimeEnd"]
                .replace(tzinfo=timezone.utc)
                .astimezone(ZoneInfo("America/Sao_Paulo"))
            )
        return myAllReserve
    
    @staticmethod
    def getNameForToken(token):
        if not isinstance(token, str):
            return None
        payload = jwtService.validateToken(token)
        return payload['name']
    
    @staticmethod
    def deleteReserve(id):
        status = db.delete_register(id)
        if status:
            return {'message': 'Sucess delete'}
        return {'error': 'Not delete'}