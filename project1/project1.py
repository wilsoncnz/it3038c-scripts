#importing the datetime module: a combination of the date and time class.
import datetime

#setting the output variable to datetime.datetime.now: creates a local instance with date and time.
output = datetime.datetime.now()

#prints todays date and time. Appends the string variables within the string. =%s. Lists in month, day, hour, minute, second for user.
print ("Today's date: %s/%s/%s" % (output.month, output.day, output.year))
print ("The current time is: %s:%s:%s" % (output.hour, output.minute, output.second))

# sources :)
# https://docs.python.org/3/library/datetime.html
# https://www.geeksforgeeks.org/python-datetime-module/
# https://www.geeksforgeeks.org/get-current-date-and-time-using-python/

