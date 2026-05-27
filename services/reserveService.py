from datetime import datetime, timezone, timedelta
from zoneinfo import ZoneInfo

class reserveService:
    @staticmethod
    def checkDateTime(_dateTimeStart: datetime, _dateTimeEnd: datetime):
        if _dateTimeEnd < _dateTimeStart:
            return {
                'sucess': False,
                'message': 'ERROR_TIME_INVALID'}
        elif _dateTimeEnd == _dateTimeStart:
            return {
                'sucess': False,
                'message': 'ERROR_TIME_EQUAL'}
        else:
            length = _dateTimeEnd - _dateTimeStart
            if length >= timedelta(hours=8):
                return {
                    'sucess': False,
                    'message': 'ERROR_TIME_OUT'}
        # horario passado
        timeNow = datetime.now(timezone.utc).replace(
            tzinfo=timezone.utc
        ).astimezone(ZoneInfo("America/Sao_Paulo"))
        if _dateTimeStart < timeNow or _dateTimeEnd < timeNow:
            return {
                'sucess': False,
                'message': 'ERROR_TIME_PAST'}
        return None