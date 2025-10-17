# Intro to Date and Times 

import datetime


date = datetime.date(2025, 1, 15)
today = datetime.date.today()
time = datetime.time(12, 30, 0)
now = datetime.datetime.now()

now1 = now.strftime("%H:%M:%S %d-%m-%Y")

print(date)
print(today)
print(time)
print(now)
print(now1)

# Exercise -- Date and time has passed the date and time 


target_datetime = datetime.datetime(2030, 1, 15, 12, 30, 1)
current_datetime = datetime.datetime.now()


if target_datetime < current_datetime:
    print("Target date has passed. ")
else:
    print("Target date has not passed. ")