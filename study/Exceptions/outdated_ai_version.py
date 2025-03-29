from datetime import datetime

months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

def get_valid_date():
    """Prompts the user for a date and returns it in YYYY-MM-DD format."""
    while True:
        date_str = input("Enter a date (MM/DD/YYYY or Month DD, YYYY): ").strip()
        try:
            if "/" in date_str:
                date_obj = datetime.strptime(date_str, "%m/%d/%Y")
                return date_obj.strftime("%Y-%m-%d")
            else:
                month_str, day_str, year_str = date_str.split()
                day_str = day_str.rstrip(",")
                month_num = months.index(month_str) + 1
                date_obj = datetime.strptime(f"{year_str}-{month_num}-{day_str}", "%Y-%m-%d")
                return date_obj.strftime("%Y-%m-%d")
        except (ValueError, IndexError):
            print("Invalid date format. Please try again.")

def main():
    """Gets a valid date and prints it in YYYY-MM-DD format."""
    formatted_date = get_valid_date()
    print(formatted_date)

if __name__ == "__main__":
    main()
