#print the pattern as follows:
# 1  
# 1 *  
# 1 * 3  
# 1 * 3 *  
# 1 * 3 * 5 
n=int(input())
for i in range(1,n*2,2):
    for j in range(1,i+1,2):
        print(j,end=" ")
    print()