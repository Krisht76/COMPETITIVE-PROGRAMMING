# 20.Python Program Using map, filter, and lambda Functions
#  Write a Python program that utilizes the map, filter, and lambda functions to achieve the following
#  objectives:
#  Use map to convert a list of integers to their corresponding squares.
#  Use filter to keep only the squared numbers that are multiples of a specific number
# WITHOUT USING SHORTHAND

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared = list(map(lambda x: x ** 2, arr))
multiple_of = 4
filtered = list(filter(lambda x: x % multiple_of == 0, squared))
print(filtered)
