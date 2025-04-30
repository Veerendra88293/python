# n=4
# k=2
# sum=0
# for i in range(n+1):      #8th
#     c=k**i
#     sum+=c    #sum of kth power of all the no
#     print(f"C({n},{i}) = {c}")

# print(f"The sum of {n},{k} is {sum}")
    

# n=100
# count=0
# for i in range(1,n+1):
#     if i%6==0 and i%8==0:# count the divisble by 6 and 8
#         count=count+1
#         print(i)
# print("total count:",count)

# n=5
# for i in range(n):
#     for j in range(i+1):
#         print(" ", end=" ")
#     for j in range(i,n-1):
#         print("*", end=" ")# w pattern
#     for j in range(n-i):
#         print("*", end=" ")
#     for j in range(i):
#         print(" ", end=" ")
#     for j in range(i):
#         print(" ", end=" ")
#     for j in range(i,n-1):
#         print("*", end=" ")
#     for j in range(n-i):
#         print("*", end=" ")
        
#     print()
    
# n=5
# for i in range(n):
#     for j in range(n):
#         if i==0 or i==n-1 or j==0 or j==n-1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# n=5
# for i in range(n):
#     for j in range(n):
#         if i+j==0 or j-i==4:
#             print("+", end=" ")
#         elif i==0 :
#             print("-", end=" ")
#         elif j==0:
#             print("|", end=" ")
#         else:
#             print(" ", end=" ")  # pattern
#         if i-j==4 or j+i==8:
#             print("+", end=" ")
#         elif i==n-1:
#             print("-", end=" ")
#         elif j==n-1:
#             print("|", end="")
#         else:
#             print(" ", end=" ")
        
#     print()

# n=5
# for i in range(n):
#     for j in range(i+1):
#         print(" ", end=" ")
#     for j in range(i,n-1):
#         print("*", end=" ")# full sand box
#     for j in range(n-i):
#         print("*", end=" ")
        
#     print()

# for i in range(n):
#     for j in range(n-i):
#         print(" ", end=" ")
#     for j in range(i):
#         print("*", end=" ")
#     for j in range(i+1):
#         print("*", end=" ")
        
#     print()

# n=4
# a=[]
# for i in range(n):
#     i=input("enter 1st ele")
#     # print(i) #print list first and last
#     a.append(i)
# print(a)
# print(a[0])
# print(a[n-1])

   
# def get_discount(bill_amount):
#     if bill_amount < 500:
#         discount = 0.05 * bill_amount
#         print(f"Discount $: {discount}")
#     elif bill_amount >=500 and bill_amount < 2500:
#         discount = 0.10 * bill_amount
#         print(f"Discount $: {discount}")  
#     else:
#         discount = 0.20 * bill_amount
#         print(f"Discount $: {discount}")
    
    
# bill_amount = int(input("Enter the bill amount $: "))
# get_discount(bill_amount)

# def count_the_vowels(input_string):
    
#     vowels="aeiouAeiou"
#     count=0
#     for i in input_string:
#         if i  in vowels:
#             count+=1
#     print(f'total vowels present is {count}times') 
            
    
    
    
# input_string = input("Enter a string: ")

# count_the_vowels(input_string)









