#input from the user and reverse the number
num = int(input("Enter a number: "))
reverse = 0
while num > 0:
    digit = num % 10          
    reverse = reverse * 10 + digit  
    num = num // 10           
print(reverse)

