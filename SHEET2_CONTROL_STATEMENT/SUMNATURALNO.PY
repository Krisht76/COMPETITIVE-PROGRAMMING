#Write a program to find the sum of all Natural numbers from 1 to N, where you have to take N as input from user 
N = int(input("Enter a positive integer N: "))
sum = 0
i = 1
while i <= N:
    sum += i
    i += 1
print(sum)