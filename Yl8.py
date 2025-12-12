
def is_leap_year(year):
    """
    Check if a year is a leap year.
    A year is a leap year if:
    - It is divisible by 400, OR
    - It is divisible by 4 AND not divisible by 100
    """
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

def is_even_year(year):
    """Check if a year is even (divisible by 2)."""
    return year % 2 == 0

def check_year(year):
    """Check if a year is leap and/or even."""
    leap = is_leap_year(year)
    even = is_even_year(year)
    
    print(f"Year: {year}")
    print(f"Leap year: {'Yes' if leap else 'No'}")
    print(f"Even year: {'Yes' if even else 'No'}")
    print()

test_years = [2000, 2024, 2100, 1900, 2023, 2025, 1600, 2001]

print("=== Year Checker ===\n")
for year in test_years:
    check_year(year)

print("=" * 40)
year_input = int(input("Enter a year to check: "))
check_year(year_input)