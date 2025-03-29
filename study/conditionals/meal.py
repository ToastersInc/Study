def main():
    time = input("What time is it? ")
    new_time = convert(time)
    if new_time >= 7 and new_time <= 8:
        print("breakfast time")
    elif new_time >= 12 and new_time <= 13:
        print("lunch time")
    elif new_time >= 18 and new_time <= 19:
        print("dinner time")
    else:
        print("not a meal time nerd")

def convert(n):
# convert string #:## or ##:## into float 
    hour, minute = n.split(":")
    hour = float(hour)
    minute = float(minute)
    minute = minute / 60
    new_time = hour + minute
    return new_time
    

if __name__ == "__main__":
    main()
