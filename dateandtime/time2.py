import datetime
import pytz

dt = datetime.datetime.now(tz= pytz.UTC)
print(dt) # this produces time with timezone.

dt_ug = dt.astimezone(pytz.timezone("Africa/Kampala"))
print(dt_ug)

for tz in pytz.all_timezones:
    print(tz)    #this is to get the list of timezones.. 