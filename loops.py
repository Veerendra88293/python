# n=5
# for i in range(n):
#     for j in range(n):
#         print("*", end=" ")
#     print()

# Right angle triangle star pattern
# n=5
# for i in range(n):
#     for j in range(i+1):
#         print("*", end=" ")
#     print()

# n=5
# for i in range(n):
#     for j in range(n-i):  #     for j in range(i,n):
#         print("*", end=" ")
#     print()
# Inverted right angle triangle star pattern


# n=5
# for i in range(n):
#     for j in range(n-i):  #     for j in range(i,n):
#         print("", end="")
#     for j in range(i+1):
#         print("*", end=" ")
#     print() 
#     n=5
#     # half full  triangle star pattern with spaces

# n=6
# for i in range(n):
#     for i in range(i+1):
#         print(" ", end=" ")
#     for j in range(n-i):
#         print("*", end=" ")
#     print()


# n=5
# for i in range(n):
#     for j in range(n-i):
#         print(" ", end=" ")
#     for j in range(i+1):
#         print("*", end=" ")
#     for j in range(i):
#         print("*", end=" ")
        
#     print()#     # full triangle star pattern with spaces


# # n=5
# # for i in range(n):
# #     for j in range(n-i):
# #         print(" ",end=" ")
# #     for j in range(i+1):
# #         print("*",end=" ")
# #     print()      


# n=5
# for i in range(n):
#     for j in range(i+1):
#         print(" ", end=" ")
#     for j in range(i,n-1):
#         print("*", end=" ")# full traaingle inverted
#     for j in range(n-i):
#         print("*", end=" ")
        
#     print()


# n=5
# for i in range(n):
#     for j in range(n-i):
#         print(" ", end=" ")
#     for j in range(i+1):
#         print("*", end=" ")
#     print()
    
# n=5
# for i in range(n):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     print()


# HALLOW TRIANGLE


# n=5
# for i in range(n):
#     for j in range(n):  #parllel bar 
#         if(j==0 or j==n-1):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# n=5
# for i in range(n):
#     for j in range(n):
#         if(i==n//2 or j==n//2):#plus sign
#             print("*",end=" ")
#         else:
#             print(" ",end=' ')
#     print()


# for i in range(5):
#     for j in range(5):
#         if(i==j or i+j==4):
#             print("*",end=" ")#cross sign  DIAGONAL
#         else:
#             print(" ",end=" ")
#     print()
    
# n=5
# for i in range(n):
#     for j in range(n):
#         if(i==0 or i==n-1 or j==0 or j==n-1):
#             print("*",end=" ")  #square sign
#         else:   
#             print(" ",end=" ")
#     print()

# n=5
# for i in range(n):
#     for j in range(i+1):
#         if(i==n-1 or j==0 or j==i):# # hollow  half triangle sign
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# n=5
# for i in range(n):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for j in range(i+1):
#         if(i==n-1 or j==0 or j==i):# # hollow half triangle sign
#             print("*",end=" ")  
#         else:
    #         print(" ",end=" ")
    # print()

# n=5
# for i in range (n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i):
#         if(i==n-1 or j==0):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     for j in range(i+1):           # # hollow inverted triangle sign
#         if(i==n-1 or j==i):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
        
#     print()


# n=5
# for i in range(n-1):
#     for j in range(n-i):
#         print(" ", end=" ")
#     for j in range(i+1):
#         print("*", end=" ")
#     for j in range(i):
#         print("*", end=" ")
        
#     print()
# n=5                                         #DIAMOND SHAPE OR RHOMBUS SHAPE
# for i in range(n):
#     for j in range(i+1):
#         print(" ", end=" ")
#     for j in range(i,n-1):
#         print("*", end=" ")
#     for j in range(i,n):
#         print("*", end=" ")
        
#     print()



# n=5
# for i in range(n-1):
#     for j in range(i,n-1):
#         print(" ", end=" ")
#     for j in range(i):
#         if(j==0):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     for j in range(i+1):
#         if(j==i):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
        
        
#     print()                                     # HA;LLOW DIAMOND SHAPE OR RHOMBUS SHAPE
# for i in range(n):
#     for j in range(i):
#         print(" ", end=" ")
#     for j in range(i,n):
#         if(j==i):
#             print("*", end=" ")
#         else:  
#             print(" ", end=" ")
        
#     for j in range(i,n-1):
#         if(j==n-2):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
        
        
#     print()

# n=7
# for row in range(n):
#     for col in range(n):
#         if(row+col==3) or (col-row==3)or(row+col==9)or(row-col==3):  #easy hallow traingle
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# n=5
# for i in range(n-1):
#     for j in range(i,n-1):
#         print("*", end=" ")
#     for j in range(i):
#         if(j==0 ):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
    
#     for j in range(i+1):
#         if(j==i):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     for j in range(i,n-1):
#         print("*", end=" ")
#     print()
# for i in range(n):
#     for j in range(i):
#         print("*", end=" ")
#     for j in range(i,n-1):
#         if(j==i):
#             print("*", end=" ")
#         else:  
#             print(" ", end=" ")
#     for j in range(i,n):
#         if(j==n-1):
#             print("*", end=" ")
#         else:  
#             print(" ", end=" ")
#     for j in range(i):
#         print("*", end=" ")
        
    # print()
    

# a=153
# b=len(str(a))
# c=[int(x) for x in str(a)]
# print(c)
# total=c[0]**b+c[1]**b+c[2]**b
# print(total)

# n=151
# conv_num=str(n)
# l=len(conv_num)
# sum=0
# for i in conv_num:   #armstrong
#     sum=sum+int(i)**l
#     print("steps:answer",sum)
# print(sum)
# if(sum==n):
#     print(" arm strong")
# else:
#     print("not arm")



# num=int(input("enter the price in notes of 2000,500,200,100:"))
# # num=4800
# n1=2000
# n2=500       #2800 money split in notes like 2000,500,200,100
# n3=200
# n4=100
# total=0
# sum=0
# exp=0
# pp=0
# while num>n1:
#     num=num-n1
#     total=total+1
# print(n1,total)
    
# while num>n2:
#     num=num-n2
#     sum=sum+1
# print(n2,sum)  
    
# while num>=n3:
#     num=num-n3
#     exp=exp+1
# print(n3,exp)
    
# while num>=n4:
#     num=num-n4
#     pp=pp+1
# print(n4,pp) 




  

# n=1500
# n1=2000
# n2=500
# n3=200
# n4=100
# total=0
# sum=0
# if n%n1==0:
    
#     print(n1) 
# elif n%n2==0:
#     sum=n//n2
# print(n2,sum)


# n=int(input("enter the number:"))
# total=0
# for i in range(1,n+1):  
#     if n%i==0:         ## factors of number
#         print(i)
#         total=total+i
# print("sum of factors:",total)







# n=6
# total=0
# for i in range(1,n+1):
#     if n%i==0:
#         total=total+i   ## factors of number
#         # print(i)
# print(total)
   
# n=6
# for i in range(1,n+1): 
#     for j in range(i): 
#         if n//i==i:         
#             print("perfect square is",i)
#     print()


# n=20
# for i in range(0,n+1):#perfect square
#     a=i**2
#     if a<=n :
#         print(a)
#     else:
#         break


   



# a=input("Enter the numbers separated by space: ")
# lar_no=""
# for i in a:                                           #largest number in list
#     if i>lar_no:
#         lar_no=i
# print("The largest number is:",lar_no)

# a=input("Enter the numbers separated by space: ")
# lar_no=a[0]
# for i in a:                                           #smALL number in list
#     if i<lar_no:
#         i=lar_no
# print("The small number is:",lar_no)



# n="veeRenDra"
# for i in n:
#     if i==i.upper():
#         print(i)
# print(n.lower())


# n=1
# m=100
# for i in range(n,m):#perfect square
#     a=i**0.5
    
#     if a==int(a):
#         print(i)
    
# n=5
# for i in range(n):
#     for j in range(n):
        
#             print("*",end=" ")
        
#     print()

# n="veerendra"
# set=0
# for char in n:
#     if char in set:
#         print("duplicate characters:",i,)
#     else:
        
#         print("unique characters:",set)
    
        

# n="siddesh"
# set=""
# count_o=0
# for i in n:
#     if i not in set:
#         set=set+i
        
#         print("count of unique characters:",set)
#     else:
#         count_o=count_o+1
#         print("duplicate characters:",count_o)



# s="ssidd"
# for i in s:
#     if s.count(i)>=2 or s.count(i)==1:      #duplicate and unique
#         print(f'{i} had duplicaate {s.count(i)}')

# n=10

# str="abc"
# str.lower()



       
    
    
    
    
    
    
    
    







        


