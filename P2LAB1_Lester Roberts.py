#CTI-110
#P2LAB1 - LAB:Driving Cost
#Lester Roberts
#9 MAY 2023
#This program will calculate driving expenses.

miles_per_gallon = float(input())
dollars_per_gallon = float(input())

dollars_per_mile = dollars_per_gallon * 1 /miles_per_gallon

miles_20 = 20 * dollars_per_mile
miles_75 = 75 * dollars_per_mile
miles_500 = 500 * dollars_per_mile

print(f'{miles_20:.2f} {miles_75:.2f} {miles_500:.2f}')


