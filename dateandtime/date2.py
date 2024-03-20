import datetime
# learning about time delta.

time_day = datetime.date.today() # here we are trying to go 7 days back from the current day.
time_delta = datetime.timedelta(days = 7)

print(f"This is 7 days back from todays date: {time_day - time_delta}")
print(f"This is 7 days  foward from todays date: {time_day + time_delta}")

# this is to see how many days are left to my birthday.
bday = datetime.date(2024,10,16)
time_left = datetime.date.today()

print(f"Time Left To My Birthday: {bday - time_left}")

till_day = bday - time_left
print(till_day.days)
print(till_day.total_seconds())