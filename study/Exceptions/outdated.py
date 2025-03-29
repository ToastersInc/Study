# In a file called outdated.py, implement a program that prompts the user for a date, anno Domini, in month-day-year order, formatted like 9/8/1636 or September 8, 1636, wherein the month in the latter might be any of the values in the list below:
from datetime import date, datetime
from re import split

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

# Then output that same date in YYYY-MM-DD format.
# If the user’s input is not a valid date in either format, prompt the user again.
# Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days.
    



def main():
    """get and check the input from the user and make sure its in month/day/year format or month day, year"""
    while True:
        try:
            date = input("Enter in a date in mm/dd/yyyy or month day, year format: ")
            if '/' in date:
                datetime.strptime(date, "%m/%d/%Y")
                formatted_date = convert_date_classic(date)
                return formatted_date

            long_date = date.split()
            if len(long_date) == 3:
                long_date[1] = long_date[1].strip(",")
                long_date[1] = int(long_date[1])
                long_date[2] = int(long_date[2])
            else:
               raise ValueError
            if long_date[0] in months and len(long_date) == 3 and long_date[1] > 0 and long_date[1] <= 31 and long_date[2] > 0 and long_date[2] <= 2025:
                formatted_date_long = convert_date_long(date)
                return formatted_date_long
        except ValueError:
            date = input("Enter in a date in mm/dd/yyyy or month day, year format: ")




def convert_date_classic(date):
    """convert mm/dd/yyyy dates into yyyy-mm-dd"""
    split_date = date.split("/")
    month = split_date[0]
    day = split_date[1]
    year = split_date[2]
    print(f"{year}-{month}-{day}")


def convert_date_long(date):
    """convert month day, year format into yyyy-mm-dd"""
    split_date = date.split()
    mon = 1
    for month in months:
        if split_date[0] != month:
            mon += 1
        if split_date[0] == month:
            break
    day = split_date[1].strip(",")
    year = split_date[2]
    print(f"{year}-{mon}-{day}")

main()
