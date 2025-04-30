# write a prg to recursivley computiond the value of A raised to the power B

# def power(A, B):
#     if B == 0:
#         return 1
#     else:
#         return A* power(A, B-1)
# A = int(input("Enter the base number: "))
# B = int(input("Enter the exponent number: "))
# result = power(A, B)
# # print("The result of A raised to the power of B is:", result)

# def fibo(n,a,b):
    

#     if n==1 or n==0:
#         print(a)
#     else:
#         print(a)                  #fibonacci series
#         print(b)
#         for i in range(2,n+2):
#             c=a+b
#             a=b
#             b=c
#             print(c)

# n=int(input("enter the string"))
# a=0
# b=1
# var1=fibo(n,a,b)
# print(var1)

#recursion for ploindrome
# def is_palindrome(s, ss, end):
#     if ss >= end:
#         return True
#     if s[ss]!=s[end]:
#         return False
#     return is_palindrome(s, start+1, end-1)

# s = input("Enter a string: ")

# result=is_palindrome(s, 0, len(s)-1)
# print("Is the string a palindrome?", result)

# n=6
# list_a=[1,2,3,4]
# list_b=[]
# for i in list_a:
#     list_b.append(i+n)
#     print(list_b)
# min_value=min(list_b)

# print(min_value)
    
# n=2
# list_a=[1,3,4,5]
# list_b=[]
# total=0
# length=len(list_a)

# for i in list_a:
#     # if n>length:
#     #     print("index out of range")
#     #     break
#     # else:
#     sorted_list=sorted(list_a)
#     list_b=sorted_list[:n]
# for j in list_b:
#     total+=j
# print(total)


# n="abcd"
# a=0
# for i in range(len(n)):
#     a=a+-1
#     print(n[a])
    
# def reverse(n,a):
    
#     # for i in range(len(n)):
        
#         a=a+-1
#         print(n[a])
            
#         return reverse(n,a)
#         # print(n[a])
#         # return reverse(n)
            
        
    

# def reverse_list(lst):
#     if len(lst) == 0:
#         return lst
#     else:
#         return lst[len(lst)-1] + reverse_list(lst[:len(lst)-1])
    
# string = "revan"

# reversed_string = reverse_list(string)
# print(reversed_string)


# list_x=input("enter the string")

# list_a=list_x.split()
# for i in list_a:
#     if list_a.count(i)>=1 and list_a.count(i)%2==1 :      #duplicate and unique
#         print(i,list_a.count(i))
#         break

# list_x=input("enter the string")

# list_a=list_x.split()
# for i in list_a:
#     if list_a.count(i)>=list_a.count(i):      #mode
#         print(i)
#         break

# list_x=input("enter the string")
# list_a=list_x.split()
# count=0
# for i in list_a:
#     if list_a.count(i)>=count:
#         mode=i
#         count=list_a.count(i)
# print(mode,count)
# k=input("enter the string")
# if k%3==0:
#     print("fizz")

# row_= int(input("Enter the number of rows: "))
# column_= int(input("Enter the number of columns: "))
# a=[]
# for i in range(row_):
#     rows=[]
#     for j in range(column_):
#         ele=int(input("enter the value for column "))
#         rows.append(ele)
#         a.append(rows)
        
# #print("/nmatrix:")
# for row_ in range(row_):
#     for j in range(column_):
#         print(a[i][j],end=" ")
#     print()


# row_= int(input("Enter the number of rows: "))
# column_= int(input("Enter the number of columns: "))
# a=[]
# for i in range(row_):
#     r=[]
    
#     for j in range(column_):           #matrix
#         ele=int(input("enter the value for column "))
#         r.append(ele)
#     a.append(r)
#     print(a)
#     n=row_
# for i in range(row_):
#     for j in range(column_):
#         if i!=j and i+j!=n-1:
#             print(a[i][j],end=" ")
            
#     print()


# row_ = int(input("Enter the number of rows: "))
# column_ = int(input("Enter the number of columns: "))

# # Input for the first matrix
# matrix_a = []
# print("Enter elements for the first matrix:")
# for i in range(row_):
#     row = []
#     for j in range(column_):
#         ele = int(input(f"Enter element for row {i+1}, column {j+1}: "))
#         row.append(ele)
#     matrix_a.append(row)

# # Input for the second matrix
# matrix_b = []
# print("Enter elements for the second matrix:")
# for i in range(row_):
#     row = []
#     for j in range(column_):
#         ele = int(input(f"Enter element for row {i+1}, column {j+1}: "))
#         row.append(ele)
#     matrix_b.append(row)

# # Display the input matrices
# print("\nMatrix A:")
# for row in matrix_a:
#     print(row)

# print("\nMatrix B:")
# for row in matrix_b:
#     print(row)

# # Multiplication of the two matrices
# result_matrix = [[0 for _ in range(column_)] for _ in range(row_)]
# for i in range(row_):
#     for j in range(column_):
#         for k in range(column_):  # Iterating over columns of A and rows of B
#             result_matrix[i][j] += matrix_a[i][k] * matrix_b[k][j]

# # Display the result matrix
# print("\nResultant Matrix after Multiplication:")
# for row in result_matrix:
#     print(row)
    

    


    
    

        
    
 
         
        