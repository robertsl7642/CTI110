# Debugging
# Lester Roberts
# CTI-110 - P3HW1
# For this assignment I was asked to debug code to enable this program to correctly takes a number grade, determines average and displays letter grade for average.


# Enter grade for six modules 

mod_1 = float(input("Enter grade for Module 1: "))
mod_2 = float(input("Enter grade for Module 2: "))
mod_3 = float(input("Enter grade for Module 3: "))
mod_4 = float(input("Enter grade for Module 4: "))
mod_5 = float(input("Enter grade for Module 5: "))
mod_6 = float(input("Enter grade for Module 6: "))

# add grades entered to a list
grades = [mod_1,mod_2,mod_3,mod_4,mod_5,mod_6]

# TO DO: determine lowest, highest , sum and average for grades 
low = min(grades)
high = max(grades)
sum = sum(grades)

# finding average = total sum by grades 
avg = sum/len(grades)

# printing in the format 
print("-----------Results------------")
print("Lowest Grade:      %.2f"%low)
print("Highest Grade:     %.2f"%high)
print("Sum of Grades:    %.2f"%sum)
print("Average:           %.2f"%low)
print("---------------------------------")

# finding perfect grade based on average
if avg >= 90:
    print("Your grade is: A")
# elif is used not else if 
elif avg > 80:
    print("Your grade is: B")
elif avg > 70:
    print("Your grade is: C")
elif avg > 60:
    print("Your grade is: D")
else:
    print("Your grade is: F")



