# Write a program to input two numbers(A & B) from the user and print the maximum element among A & B. 
A = int(input("Enter first number:"))
B =int(input("Enter second number:"))
if A > B:
    print("a is maximum")
elif B > A:
    print("b is maximum")
else:
    print("invalid number")
