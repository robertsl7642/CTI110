# This program provides an Output range with increments of 5
# P4LAB2
# Lester Roberts
# CTI-110


num1 = int(input())
num2 = int(input())


if num1 <= num2:
    while num1 <= num2:
        print(num1, end=' ')
        num1 += 5
    print()
else:
    print('Second integer can\'t be less than the first.')

