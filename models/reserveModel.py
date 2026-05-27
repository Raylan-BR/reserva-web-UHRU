from database.DatabaseMongoDb import db
from datetime import datetime, timezone
from zoneinfo import ZoneInfo
from services.jwtService import jwtService
from services.reserveService import reserveService

class reserveModel:  
    @staticmethod
    def createReserve(dateTimeStart, dateTimeEnd):
        __name = jwtService.getNameForToken(
            jwtService.getTokenRequest()
        )
        __time = reserveModel.validateDateTime(
            dateTimeStart,
            dateTimeEnd
        )
        try:
            db.create_register(
                __name, __time['start'], __time['end'])
            
            return {
                'sucess': True,
                'message': 'SUCESS_CREATE_RESERVE'}
        except Exception as e:
            print(f'Error in create reserve: {e}')
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
            searchReserve = reserveModel.__timeOverlap(_dateTimeStart, _dateTimeEnd)
            if searchReserve:
                return {
                    'sucess': False,
                    'message': 'ERROR_TIME_EXIST',
                    'reserve': searchReserve}

            # Passou pela validação            
            return {
                    'sucess': True,
                    'start': _dateTimeStart,
                    'end': _dateTimeEnd
                }
        
        except Exception as e:
            print(f'Error in validate DateTime: {e}')
            return {
                'sucess': False,
                'message': 'ERROR_TIME_CONVERT'}
        
    @staticmethod
    def __timeOverlap(dateTimeStart, dateTimeEnd):
        return db.exist_reserve(dateTimeStart, dateTimeEnd)

    @staticmethod
    def getAllReserve():
        allReserve = db.get_all_register()

        for reserve in allReserve:
            reserve.pop('_id', None)

        return allReserve
    
    @staticmethod
    def getMyAllReserve():
        name = jwtService.getNameForToken(
            jwtService.getTokenRequest()
        )
        myAllReserve = db.get_all_register({'name': name})
        return myAllReserve
    
    @staticmethod
    def deleteReserve(id):
        name = jwtService.getNameForToken(
            jwtService.getTokenRequest()
            )
        status = db.delete_register(id, name)
        if status:
            return {
                'sucess': True,
                'message': 'SUCESS_DELETE'}
        return {
            'sucess': False,
            'message': 'ERROR_NOT_DELETE'}