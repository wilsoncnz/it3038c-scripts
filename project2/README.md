# PROJECT 2 
## Specific U.S. Time Zone Times
For Project 1, I created a simple code that displayed the current time in military time, with no AM or PM. 

For Project 2, I decided to add to Project 1 and simplify the time to AM or PM, in hh:mm:ss AM/PM. It will also list today's late in MM/DD/YYYY

Furthermore, I will add different time zone choices in 
which the code will prompt the user to ask for the respective U.S. time zone, and it will output the time accordingly. The <code> import datetime</code> feature seemed to only display UK
London time. So, UK will be the default time listed in the instance the user misspells or does not capitalize correctly.

### Note: The Output up until november 7th will be off by one hour due to the difference in observed daylight savings between the US and the UK (which datetime uses as a basis)

Daylight Savings Time in the UK starts October 31st, in the US it starts November 7th, so for those few days it will be off by one hour.


## Code: 

The code will start by prompting the user to input what time zone they are in. It will specify to the user that it is US only, and that it is case sensitive.


<code> print ("US timezones include: 'Hawaiian', 'Alaskan', 'Pacific Time', 'Mountain Time', 'Central Time', 'Eastern Time'") </code>

<code> timezone=input("What time zone are you in? (US Only and case sensitive) ") </code>

After the user inputs their respective U.S. timezone, it will output the the date in MM/DD/YYYY and the time in HH:MM:SS AM or PM.

#### Here is an example of a successful input output function:
US timezones include: 'Hawaiian', 'Alaskan', 'Pacific Time', 'Mountain Time', 'Central Time', 'Eastern Time'

What time zone are you in? (US Only and case sensitive) 

Eastern Time

Today's date: 10/31/2021
The current time is: 5:57:55 PM

#### Sources:
https://docs.python.org/3/library/datetime.html

https://www.geeksforgeeks.org/python-datetime-module/

https://www.geeksforgeeks.org/get-current-date-and-time-using-python/

https://www.timeanddate.com/time/map/

https://www.timeanddate.com/time/zone/usa

