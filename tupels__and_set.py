# thistuple = ("apple", "banana", "cherry", "apple", 1)
# print(thistuple)
# s1,s2,s3,s4,s5=thistuple
# print(s1)

# a=1,2,3,"apple"
# print(a)
# print(type(a))

# thisset = {"apple", "banana", "cherry", "apple"}
# print(id(thisset))
# thisset.add("orange")
# thisset.update(["mango", "grapes"])
# print(id(thisset))


# print(thisset)

# num_list = [(10,20,30),(1,2),(5,10,15,45)]
# set_list = tuple(num_list)
#     # print(set_list)
# s1,s2,s3=set_list
# set_s1=list(s1)
# print(set_s1.pop(2))
# # print(set_s1)
# set_s1.append(40)

# print(set_s1)

# num_list = [(10,20,30),(1,2),(5,10,15,45)]
# for i in num_list:
#     i=list(i)
#     i.pop()
#     i.append(40)
#     i=tuple(i)
#     print(i)


# list_a = input("Enter the numbers separated by space: ")

# list_a = list_a.split()
# list_b = []
# for i in list_a:
#     if i not in list_b:
#         list_b.append(i)
#         print(i)
# list_b.sort()


# set_a = {"pencil"}
# word = input()
# set_a.add(word)
# list_a = list(set_a)
# list_a.sort()
# print(list_a)



# dictionary = {"name": "John", "age": 30, "city": "New York"}
# print(dictionary["age"])
# print(dictionary.items())
# dictionary["city"] = "Los Angeles"
# print(dictionary)

# dictionary = {"name": "John", "age": 30, "city": "New York","place":{ "country":"USA", "state":"California"  }}
# print(dictionary["age"])
# print(dictionary.items())
# dictionary["city"] = "Los Angeles"
# print(dictionary)
# print(dictionary["place"]["country"])
# del dictionary["name"]

# print(dictionary)
student={
    "ram":"cricekt",
    "narsh":"cricekt",
    "vai":"cricekt",
    "rohan":"cricekt",
    
}
n=2
k=[]
#add list of tuples to dictionary
# tuples=[("Mikey","cricekt"), ("rahull","football"), ("sideesh", "chess"), ("rohan", "basketball")]
for i in range(n):
    key = input("Enter name: ")
    value = input("Enter sports: ")
    k.append((key,value))
print(k)
    # k.append(value)
    
# tuples_list=tuple(k)
#     # print(tuples_list)
for i in range (0,len(k)):
    student[k[i][0]]=k[i][1]
    
    # student[key]=value
# # print(tuples_list)
# # print(k)
print(student)

    
    
    
    # key = input("Enter key: ")
    # value = input("Enter value: ")
    # dictionary[key] = value

