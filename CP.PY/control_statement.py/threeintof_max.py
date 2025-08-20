#q7)  Read three integers and print their maximum.
# Read three integers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("The maximum number is a")
elif b >= a and b >= c:
    print("The maximum number is b ")
else:
    print("The maximum number is c")