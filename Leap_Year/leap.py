# Leap Year

# Take a year as input and figure out if it's a leap year or not.

# This is how you work out whether if a particular year is a leap year.

# on every year that is divisible by 4 with no remainder

# second condition:
# except every year that is evenly divisible by 100 with no remainder

# third condition: (continuous condition)
# unless the year is also divisible by 400 with no remainder

# e.g. The year 2000:
# 2000 ÷ 4 = 500 (Leap)
# 2000 ÷ 100 = 20 (Not Leap)
# 2000 ÷ 400 = 5 (Leap!)
# So the year 2000 is a leap year.

# But the year 2100 is not a leap year because:
# 2100 ÷ 4 = 525 (Leap)
# 2100 ÷ 100 = 21 (Not Leap)
# 2100 ÷ 400 = 5.25 (Not Leap)

year = int(input("Enter the year: "))
is_leap_year = False

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            is_leap_year = True
        else:
            is_leap_year = False

    else:
        is_leap_year = True

if is_leap_year:
    print(f"Year {year} is a leap year!")
else:
    print(f"Year {year} is NOT a leap year.")
