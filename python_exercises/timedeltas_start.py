#
# Example file for working with timedelta objects
#

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

# construct a basic timedelta and print it
print(timedelta(days = 365, hours = 5, minutes = 1))


# print today's date
now = datetime.now()
print('today is: ' + str(now))

# print today's date one year from now
print('one year from now will be: ' + str(now + timedelta(days = 365)))

# create a timedelta that uses more than one argument
print("In 2 days and 3 weeks, it will be " + str(now + timedelta(days = 2, weeks = 3)))

# calculate the date 1 week ago, formatted as a string
t = datetime.now() - timedelta(weeks = 1)
# to = date.today() - timedelta(weeks = 1)
s = t.strftime("%A %B %d, %Y")
# so = to.strftime("%A %B %d, %Y")
print("one week ago it was: ", t)
# print("one week ago it was: ", to)
print("one week ago it was: ", s)
# print("one week ago it was: ", so)

### How many days until April Fools' Day?
today = date.today()
afd = date(today.year, 4, 1)


# use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year
if afd < today:
    print("April Fools' past %d days ago" % ((today - afd).days))
    afd = afd.replace(year = today.year+1)
    print(afd, "is the next April Fools")

# Now calculate the amount of time until April Fool's Day  
time_til = afd - today
print(time_til.days, "days left until April fools")

