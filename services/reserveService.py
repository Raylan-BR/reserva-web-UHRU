from datetime import datetime, timezone, timedelta
from zoneinfo import ZoneInfo

class reserveService:
    @staticmethod
    def checkDateTime(_dateTimeStart: datetime, _dateTimeEnd: datetime):
        if _dateTimeEnd < _dateTimeStart:
            return {'error': 'Time invalid'}
        elif _dateTimeEnd == _dateTimeStart:
            return {'error': 'Time equal'}
        else:
            length = _dateTimeEnd - _dateTimeStart
            if length >= timedelta(hours=8):
                return {'error': 'Time out'}
        # horario passado
        timeNow = datetime.now(timezone.utc).replace(
            tzinfo=timezone.utc
        ).astimezone(ZoneInfo("America/Sao_Paulo"))
        if _dateTimeStart < timeNow or _dateTimeEnd < timeNow:
            return {'error': 'Time past'}
        return None
        