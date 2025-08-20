#Take an integer N as input. Your task is to calculate and print the sum of the digits of the given number N.
N = int(input("Enter an integer N: ")) 
Sum = 0
while N > 0:
    Sum += N % 10
    N //= 10
print(Sum)