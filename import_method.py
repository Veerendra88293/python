# import math 
# print(math.sqrt(4))


# # from math import sqrt
# # print(sqrt(4))

# from math import *
# print(sqrt(4)*pi)

# from math import sqrt as s
# print(s(4))0

# import math
# print(dir(math))  # list all the attributes and methods of math module

# from function_prog import *
# print(function_name)   #importing from my other file

# import numpy
# arr=numpy.array([[1,2,3,4,5],[6,7,8,9,10]])
# print(arr)

import numpy
# Taking input for the number of rows and columns
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
# Initializing an empty list to store the rows
data = []
# Taking input for each row
for i in range(rows):
    row = list(map(int, input(f"Enter the elements for row {i+1}, separated by spaces: ").split()))
    data.append(row)
# Converting the list of lists into a NumPy array
arr = numpy.array(data)
# Printing the NumPy array
print("The NumPy array is:")
print(arr)

# Calculating the sum of all elements in the array

# print("Sum of all elements:", numpy.sum(arr))


