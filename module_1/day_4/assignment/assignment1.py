#  create a program that checks if a given year is a leap year. Print message indicating whether it is or not.

year = int(input("Enter a year: "))

def check_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f"{year} is a leap year.")
            else:
                print(f"{year} is not a leap year.")
        else:
            print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")

check_leap_year(year)