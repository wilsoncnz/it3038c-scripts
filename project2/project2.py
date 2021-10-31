#import the function used to get the date and time

import datetime

output = datetime.datetime.now()

#get user input

print ("US timezones include: 'Hawaiian', 'Alaskan', 'Pacific Time', 'Mountain Time', 'Central Time', 'Eastern Time'")

timezone=input("What time zone are you in? (US Only and case sensitive) ")

#check timezone input and change time accordingly

if timezone == "Hawaiian":

  hour = output.hour - 10

 

elif timezone == "Alaskan":

  hour = output.hour - 9

 

elif timezone == "Pacific Time":

  hour = output.hour - 8

 

elif timezone == "Mountain Time":

  hour = output.hour - 7

 

elif timezone == "Central Time":

  hour = output.hour - 6

 

elif timezone == "Eastern Time":

  hour = output.hour - 5

 

#output to the user the default UK time in the instance they mispell or do not capitalize the given US timezones

else:

  hour = output.hour

  minute = output.minute

  second = output.second

 

  if hour >= 13:

    hour = hour - 12

    minute = output.minute

    second = output.second

    morning = " PM"

 

  else:

    hour = hour

    minute = output.minute

    second = output.second

    morning = " AM"

 

  print ("You have entered an invalid timezone name, London time will be shown by default.")

  print ("Today's date: %s/%s/%s" % (output.month, output.day, output.year))

  print ("The current time is: %s:%s:%s" % (hour, minute, second) + morning)

#change hour count from military time to AM/PM time

if hour >= 13:

  hour = hour - 12

  minute = output.minute

  second = output.second

  morning = " PM"

 

else:

  hour = hour

  minute = output.minute

  second = output.second

  morning = " AM"

#Note output up until november 7th will be off by one hour due difference in observed daylight savings between the US and the UK (which datetime uses as a basis)

print ("Today's date: %s/%s/%s" % (output.month, output.day, output.year))

print ("The current time is: %s:%s:%s" % (hour, minute, second) + morning)