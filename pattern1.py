# print this pattern as follows:
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * *
n=int(input())
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()