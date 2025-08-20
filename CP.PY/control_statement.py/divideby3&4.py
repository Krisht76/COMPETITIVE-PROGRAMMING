#q2) check if the number is divisible by 3 and last digit is 4.?

num = int(input("Enter a number: "))

if num % 3 == 0 and num % 10 == 4:
    print("Number is divisible by 3 and last digit is 4")
else:
    print("Number is not divisible by 3 or last digit is not 4")