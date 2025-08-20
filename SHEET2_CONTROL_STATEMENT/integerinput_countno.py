# Take an integer N as input and print the count of digits of that number.
N = int(input("Enter an integer N: "))
count = 0
while N > 0:
    count += 1
    N //= 10
print(count)