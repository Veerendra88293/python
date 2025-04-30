a=input("Enter the no: ")
# print(f'input is {a}')
try:
    # for i in range(len(a)):
    #     print(a[i])
    a=int(a)
    print(f'Square of {a} is {a**2}')
except Exception as e: #us eonlt except also
    print("hi")
