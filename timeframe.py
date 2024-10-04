from typing import Literal
import datetime as dt
from datetime import datetime


class Timeframe:
    def __init__(self, 
                 tf: str, 
                 tz: dt.timezone = dt.timezone.utc,
                 format: Literal['datetime', 'unixtime'] = 'unixtime'):
        self.tf = tf
        self.tz = tz
        self.format = format

    def _by_seconds(self, 
                    seconds: int,
                    throuth: int):
        unix_now = int(datetime.now(self.tz).timestamp())
        return seconds * (unix_now // seconds + throuth)
        
    def _by_months(self, throuth: int = 1):
        now = datetime.now(self.tz)
        delta_month = (now.year - 1970) * 12 + now.month 
        interval = int(self.tf.replace('M', ''))
        steps = delta_month // interval
        month = (steps + throuth) * interval % 12
        month = 1 if month == 0 else month
        year = 1970 + (((steps + throuth) * interval) // 12)
        return int(datetime(year, month, 1, tzinfo=self.tz).timestamp())
    
    def _by_years(self, throuth: int = 1):
        now = datetime.now(self.tz)
        delta_year = now.year - 1970
        interval = int(self.tf.replace('y', ''))
        steps = delta_year // interval
        year = 1970 + (steps + throuth) * interval
        return int(datetime(year, 1, 1, tzinfo=self.tz).timestamp())

    def throuth(self,
                throuth: int = 1, # next
                format: Literal['datetime', 'unixtime', 'self'] = 'self'):
        tf = self.tf.lower() if not self.tf.endswith('M') else self.tf
        try:
            match tf[-1]:
                case 's': unix_throuth = self._by_seconds(int(tf.replace('s', '')), throuth)
                case 'm': unix_throuth = self._by_seconds(int(tf.replace('m', '')) * 60, throuth)
                case 'h': unix_throuth = self._by_seconds(int(tf.replace('h', '')) * 3600, throuth)
                case 'd': unix_throuth = self._by_seconds(int(tf.replace('d', '')) * 86400, throuth)
                case 'w': unix_throuth = self._by_seconds(int(tf.replace('w', '')) * 604800, throuth)
                case 'M': unix_throuth = self._by_months(throuth)
                case 'y': unix_throuth = self._by_years(throuth)
        except:
            raise ValueError(self.tf)
        format = self.format if format == 'self' else format
        if format == 'datetime':
            return datetime.fromtimestamp(unix_throuth, self.tz)
        elif format == 'unixtime':
            return unix_throuth
        
    def next(self,
             format: Literal['datetime', 'unixtime', 'self'] = 'self'):
        return self.throuth(throuth=1, format=format)
    
    def current(self,
                format: Literal['datetime', 'unixtime', 'self'] = 'self'):
        return self.throuth(throuth=0, format=format)
    
    def previous(self,
                 format: Literal['datetime', 'unixtime', 'self'] = 'self'):
        return self.throuth(throuth=-1, format=format)
    
    def to_seconds(self):
        tf = self.tf.lower() if not self.tf.endswith('M') else self.tf
        try:
            match tf[-1]:
                case 's': return int(tf.replace('s', ''))
                case 'm': return int(tf.replace('m', '')) * 60
                case 'h': return int(tf.replace('h', '')) * 3600
                case 'd': return int(tf.replace('d', '')) * 86400
                case 'w': return int(tf.replace('w', '')) * 604800
            return None
        except:
            raise ValueError(self.tf)
