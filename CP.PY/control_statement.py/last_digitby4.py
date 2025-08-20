#q1) This script checks if the last digit of a given number is 4

num = int(input("Enter a number: "))
if num % 10 == 4:
    print("Last digit is 4")
else:
    print("Last digit is not 4")