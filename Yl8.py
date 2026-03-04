def is_leap_year(year):
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

def check_year(year):
    if is_leap_year(year):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")

    if year % 2 == 0:
        print(f"{year} is even")
    else:
        print(f"{year} is odd")
    print()

test_years = [2000, 2024, 2100, 1900, 2023]

for year in test_years:
    check_year(year)

year = int(input("Enter a year: "))
check_year(year)