# # """
# # Take a year as input. Check if it is a leap year. A year is a leap year if it is divisible by 4, but not by 100, unless it is also divisible by 400

# # """

# # year = int(input("Enter year "))

# # if year %4==0:
# #     print(f"{year} is a leap year")

# # else:
# #     print(f"{year} Not a leap year")    

# """
# Take a year as input. Check if it is
# """
# """import calendar

# print(calendar.isleap(200))"""

'''
Take a year as input. Check if it is a leap year. A year is a leap year if it is divisible by 4, but not by 100, unless it is also divisible by 400.

200 - not a leap year
204 - leap
800 - leap year

'''
year = int(input("Enter year = "))

if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
     print("Leap Year")
else:
     print("Not a leap year")     

