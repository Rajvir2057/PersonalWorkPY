# here only time is being used...

import datetime

time = datetime.time(9,30,33,100000) #here we are working with hours min sec and micro sec...
print(time)
print(time.hour)
dateandtime = datetime.datetime(2024,3,20,10,30,20,100000)
print(dateandtime,"\n")

dt_today= datetime.datetime.today()
dt_now= datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

print(dt_today)# returns local time 
print(dt_now) # returns local time with a timezone if filled
print(dt_utcnow)# gives current time with time zone..