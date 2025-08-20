#Write a program to print all Natural numbers from N to 1, where you have to take N as input from the user. 
N = int(input("Enter a positive integer N: "))
i = N
while i >= 1:
    print(i)
    i -= 1