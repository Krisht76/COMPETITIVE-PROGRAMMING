# 1.Keyword arguments
#  Define a function in Python Introduce , providing their name, age, and profession as arguments.
N = int(input())
for _ in range(N):
    data = input().split()
    name = data[0]
    age = data[1]
    profession = data[2]
    print(f"{profession} {name}, age {age}")
    