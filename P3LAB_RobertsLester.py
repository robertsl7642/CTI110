#CTI-110
#P3LAB - Leap Year
#Lester Roberts
#9 May 2023



# A flag variable to assume not a leap year at the beginning
is_leap_year = False

# Input the year
input_year = int(input())

# Set is_leap_year to true if the input year is a leap year
if input_year % 4 == 0:  # if the input year is divisible by 4
    if input_year % 100 == 0:  # if the input year is divisible by 100
        if input_year % 400 == 0:  # if the input year is divisible by 400
            is_leap_year = True  # set is_leap_year to true
    else:
        is_leap_year = True  # set is_leap_year to true


# TODO: Output the result based on the value of is_leap_year
if is_leap_year:  # if is_leap_year is true
    print(input_year, "- leap year")
else:  # if is_leap_year is false
    print(input_year, "- not a leap year")
