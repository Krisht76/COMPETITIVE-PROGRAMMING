#Take an integer A as input. You have to print the sum of all odd numbers in the range [1, A].
A = int(input("Enter a positive integer A: ")) 
odd = 0
i = 1
while i <= A:
    if i % 2 != 0: 
        odd += i
    i += 1
print(odd)
