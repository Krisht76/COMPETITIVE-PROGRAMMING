#  19.Convert Names to Lowercase Using Map and Lambda Function
#  Create a Python program that accomplishes the following tasks:
#  Define a list names containing string values.
#  Use the map() function with a lambda function to convert each name in the list names to
#  lowercase.
#  Store the modified names in a variable result.
#  Print the result list

names = ["Alice", "Bob", "Charlie", "David"]
result = list(map(lambda x: x.lower(), names))
print(result)
