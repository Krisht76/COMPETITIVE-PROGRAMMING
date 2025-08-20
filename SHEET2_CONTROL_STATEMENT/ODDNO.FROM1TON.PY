#Write a program to print all odd numbers from 1 to N, where you have to take N as input from user. 
N = int(input("Enter a positive integer N: "))
i = 1
while i <= N:
    if i % 2 != 0:
        print(i)
    i += 1