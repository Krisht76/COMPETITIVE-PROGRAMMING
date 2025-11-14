# 17.Filter Even No with lambda fucntion
#  Create a Python program that accomplishes the following tasks:
#  Define a list arr containing integer values.
#  Use the filter() function with a lambda function to filter out the even numbers from the list
#  arr.
#  Store the filtered values in a variable ans.
#  Print the ans list

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ans = list(filter(lambda x: x % 2 == 0, arr))
print(ans)
