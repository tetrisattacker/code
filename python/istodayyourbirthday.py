#Import datetime library
from datetime import *

#Get Today's Date
today = date.today()

#Get User's Birthday
dob_str = input("What is your Date of Birth? dd/mm/yyyy")

#Convert user input into a date
dob_data = dob_str.split("/")
dobDay = int(dob_data[0])
dobMonth = int(dob_data[1])
dobYear = int(dob_data[2])
dob = date(dobYear, dobMonth, dobDay)
#Determine if today is the user's birthday
thisYear = today.year
nextBirthday = date(thisYear, dobMonth, dobDay)

if today == nextBirthday:
    print("Happy Birthday!")
else:
    print("Today is not your birthday.")