#  2.Default argument
#  WAPtodefine and utilize a Python function named introduce to print out information about
#  individuals, including their name, age, and profession, with an optional default value for the
#  profession parameter.
N = int(input())
for _ in range(N):
    data = input().split()
    name = data[0]
    age = data[1]
    profession = data[2] if len(data) > 2 else "Unemployed"
    print(f"{profession} {name}, age {age}")
    