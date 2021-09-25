from datetime import datetime



now = datetime.now()
now=str(now)

nowYear = now[0:4]
nowMonth = now[5:7]
nowDay = now[8:10]
nowHours = now[11:13]
nowMinutes = now[14:16]
nowSeconds = now[17:19]

nowYear = int(nowYear)
nowMonth = int(nowMonth)
nowDay = int(nowDay)
nowHours = int(nowHours)
nowMinutes = int(nowMinutes)
nowSeconds = int(nowSeconds)


print("now =", now)


print('What is your month of birth?')
month = input()
month = int(month)
print('What is your day of birth?')
day = input()
day = int(day)
print('What is your year of birth?')
year = input()
year = int(year)
hour = 12
minutes = 00
seconds = 00



if month == 1 or 3 or 5 or 7 or 8 or 10 or 12:
    monthDays = 31
elif month == 2:
    monthDays = 28
elif month == 4 or 6 or 9 or 11:
    monthDays = 30

difYear = nowYear - year
difMonth = nowMonth - month
difDay = nowDay - day
difHour = nowHours - hour
difMinutes = nowMinutes - minutes
difSeconds = nowSeconds - seconds


monthSeconds = difMonth * monthDays * 24 * 60 * 60
daySeconds = difDay * 24 * 3600
yearSeconds = difYear * 365 * 24 * 3600
totalSeconds = monthSeconds + daySeconds + yearSeconds

print(totalSeconds)