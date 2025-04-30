from datetime import date, timedelta
import sys
import inflect

#get input from user

def main():
    try:
        year = int(input("Year: "))
        month = int(input("Month: "))
        day = int(input("day: "))
        birthday = date(year, month, day)
    except ValueError:
        sys.exit("date format must be in YYYY-MM-DD")

    # get difference between birthday and today in minutes
    difference = abs(date.today() - birthday)
    minutes = difference.total_seconds() / 60

    # print difference in english 
    p = inflect.engine()
    print(f"You were born", p.number_to_words(int(minutes)), "minutes ago")

if __name__ == "__main__":
    main()