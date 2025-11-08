#TIP never name the files like the packages it will give you an circular import error
#this is the practice for the date time activities.

from datetime import datetime,date,time,timedelta

#our first approach to this package is to create an object 

#lets see what gives us this:
dt = datetime.now()

print("our first object of datetime: ",dt)

#one of the benefits of these object are that you can decompose the elements once you have created the object

print("the year of the dt object is: ",dt.year)
print('the month is :',dt.month)
print('the day is: ',dt.day)

#also you can decompose the time in each individual element

print(f"the hour is {dt.hour}, the minutes are {dt.minute}, seconds {dt.second} and microsecond are {dt.microsecond}")

#another way to create ojects datetime is defining the data by ourserlves 

mydatetime = datetime(2030,1,1,00,00,1)

print("this is the date of the back to future arrival: {}".format(mydatetime))

#we can do a replace of the date by passing some values to the method. But we need to assign again the value to the same variable.

mydatetime = mydatetime.replace(year=2035)

print("now we can see the new year: ",mydatetime)

#by default there is a format that we can use to show the date and time like this

print("now using the iso format",mydatetime.isoformat())

#we have special classes that will make the format in string some more readable 

print(mydatetime.strftime("%A %d %B %Y %I:%M")) #this will format the date in text not numbers

#you can play with some of the variables to the location this can make that language is setup to different regions

import locale
#this will change the current language
locale.setlocale(locale.LC_ALL,'es_MX.UTF-8')

#now lets print again the date time with text 

print(mydatetime.strftime("%A %d %B %Y %I:%M")) #this will format the date in text not numbers but now using the locale settings

#one of the great things is that we can do operations with date and time to add more years, days or hours to an specific area.

#we need to create a type delta with the exra time that we want to add

mydelta = timedelta(days=1)

print(f"the added time that we want is {mydelta} and I want to added to this {mydatetime} so the result is {mydelta+mydatetime}")
