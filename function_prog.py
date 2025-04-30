# def function_name():
#     print("Hello, World!")
#     return
    
# var=function_name()
# print(var)

def function_name():
    msg="Hello, World!"
    return msg
    
var=function_name()
print(var)
print(type(var))

# def function_name():
#     for i in range(1,10):
#         return i
#         print(i,end=" ")
        
        
# print(function_name())







# def function_name(name):
#     n=5
#     for i in range(n):
#         for j in range(n):
#             print(name,end="")

#         print()
# first_name=input("Enter first name:")
# function_name(first_name)







# n=5
# for i in range(0,n+1):

#     for j in range(n-i):
#         print(" ",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")

#     print()



# def addition(a,b):
#     c=a+b
#     print("Addition of two numbers is:",c)
    
# a=int(input("Enter first number:"))
# b=int(input("Enter second number:"))
# addition(a,b)

# def add(a, b):
#     return a + b

# result = add(3, 4)
# print(result)

# def calculator(a, b, operation):
#     if operation == '+':
#         return a + b 
#     elif operation == 'subtract':
#         return a - b
#     elif operation == 'multiply':
#         return a * b
#     elif operation == 'divide':
#         return a / b
#     else:
#         return "Invalid operation"
    
# a=int(input("Enter first number:"))
# b=int(input("Enter second number:"))
# operation=input("Enter operation (add, subtract, multiply, divide):")
# result=calculator(a, b, operation)
# print(result)

# def numbers(a):
#     if a%2==0:
#         print("even number")
#     else:
#         print("odd number")
#         return
    
# a=int(input("enter the number to check"))
# numbers(a)




    
# def palindrome(a):
#     m=a[::-1]
#     if a==m:
#         print("polindrom")
#     else:
#         print("not")
        
# a="121"
# palindrome(a)

# def palindrome(m):
#     # m=fruits.reverse()
#     # print(fruits)
#     if m==m.reverse():
#         print("polindrom")
#     else:
#         print("not")
        
# fruits = 123
# m=list(str(fruits))
# palindrome(m)

# def armstrong(n):
#     m = len(str(n))
#     kk = 0
#     for digit in str(n):
#         kk += int(digit) ** m

#     if kk == int(n):
#         print("Armstrong number")
#     else:
#         print("Not an Armstrong number")

# n = 153
# armstrong(n)

# def bbbb(i):
#     for i in range(1, 10):
#         print(i, end=" ")
        
# bbbb()

# def fun(xyz):
#     xyz+=["hello"]
#     return xyz
    
# fruits = ["apple", "banana", "cherry"]
# print(fruits)
# var=fun(fruits)

# print(var)

def onlynumber(input_str):
    words = input_str.split()
    numbers = []
    for i in words:
        if i.isdigit():
            numbers.append(float(i))
        elif i.replace('.', '', 1).isdigit():
            numbers.append(float(i))
    numbers.sort()
    
    
    return numbers

input_str = input("Enter input: ")
sorted_numbers = onlynumber(input_str)
print(sorted_numbers)
print(min(sorted_numbers))
print(max(sorted_numbers))
#code for max