
from datetime import datetime
from datetime import date

today_date = datetime.today()
print("Todays date is: ", today_date)
print("Days till birthday")
#user's birthday
your_birthday = input("When is your birthday (yyyy-mm-dd): " )
your_birthday = datetime.strptime(your_birthday, "%Y-%m-%d")
print(your_birthday)
#todays date
today_date = datetime.today()
print("Todays date is: ", today_date)

days_till = your_birthday - today_date
print(days_till)

print("Todays date is: ", today_date)
date_of_birth = input("when were you born?: ")
date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d")
print(date_of_birth)

age = today_date - date_of_birth
age1 = age // 365
print(age1,"years")
