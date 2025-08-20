#q3) read a number and check if the number is divisible by 7 or last digit is 5.

num = int(input("Enter another number: "))
if num % 7 == 0 or num % 10 == 5:
    print("Number is divisible by 7 or last digit is 5")
else:
    print("Number is not divisible by 7 and last digit is not 5")