#importing the datetime module: calls for the date and time objects to supply classes
import datetime
output = datetime.datetime.now()

#setting the output variable to a class date.time.datetime.now - combines date and time with date time attributes
print ("Today's date: %s/%s/%s" % (output.month, output.day, output.year))
print ("The current time is: %s:%s:%s" % (output.hour, output.minute, output.second))

# sources :)
# https://docs.python.org/3/library/datetime.html
# https://www.geeksforgeeks.org/python-datetime-module/
# https://www.geeksforgeeks.org/get-current-date-and-time-using-python/

