from datetime import datetime, timezone, timedelta
from zoneinfo import ZoneInfo

class reserveService:
    @staticmethod
    def checkDateTime(_dateTimeStart: datetime, _dateTimeEnd: datetime):
        if _dateTimeEnd < _dateTimeStart:
            return {
                'sucess': False,
                'message': 'Error time invalid'}
        elif _dateTimeEnd == _dateTimeStart:
            return {
                'sucess': False,
                'message': 'Error time equal'}
        else:
            length = _dateTimeEnd - _dateTimeStart
            if length >= timedelta(hours=8):
                return {
                    'sucess': False,
                    'message': 'Error time out'}
        # horario passado
        timeNow = datetime.now(timezone.utc).replace(
            tzinfo=timezone.utc
        ).astimezone(ZoneInfo("America/Sao_Paulo"))
        if _dateTimeStart < timeNow or _dateTimeEnd < timeNow:
            return {
                'sucess': False,
                'message': 'Error time past'}
        return None