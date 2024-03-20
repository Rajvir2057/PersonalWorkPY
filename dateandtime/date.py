#import date and time module as shpwn below.
import datetime

#naive date, do not have time zone or any detail.
#1 

day = datetime.date(2024,3,20) # if u add a leading 0 it pull out an error for month and day.
print(day)

#2 

day2 = datetime.date.today()
print(day2)

# to print just year, month or day,

print(day2.year)
print(day2.day)
print(day2.month)

#to get a weekday.. 
print(day2.weekday()) # FOR WEEKDAY MONDAY IS 0 AND SUNDAY IS 6
print(day2.isoweekdAY()) # FOR THE ISOWEEKDAY MONDAY IS 1 AND SUNDAY IS 7




