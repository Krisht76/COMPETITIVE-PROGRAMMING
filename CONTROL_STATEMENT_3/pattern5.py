#print the pattern as follows:
# *_ _ _* 
# *_ _ _* 
# *_ _ _* 
# *_ _ _* 
# *_ _ _*
n=int(input())
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()