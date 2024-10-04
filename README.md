# tfmanager

tfmanager is easy-to-use python script to interaction with timeframes
## Features
* support output as unixtime and datetime objects
* support timezone offset
* support seconds (s), minutes (m), hours (h), days (d), weeks (w), months (M) and years (y) timeframes
* support get time of start for all timeframe steps by ```throuth``` method
* support get total seconds of timeframe by ```to_seconds``` method (not working for months and years timeframes)
## Quickstart
```python
from datetime import datetime, timedelta
from tfmanager import Timeframe

tz = dt.timezone(timedelta(hours=4))
tf = Timeframe('1h', tz, 'datetime')

print(datetime.now(tz))
print(tf.next())
print(tf.current())
print(tf.previous())
print(tf.throuth(4))
print(tf.to_seconds())

# 2024-10-04 15:31:44.248618+04:00
# 2024-10-04 16:00:00+04:00
# 2024-10-04 15:00:00+04:00
# 2024-10-04 14:00:00+04:00
# 2024-10-04 19:00:00+04:00
# 3600
```

## Contacts
**Telegram:** [@TheDinAlt](https://t.me/TheDinAlt)

`with 💜 by TheDinAlt`
