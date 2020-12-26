#45*3=555,56+9=77,56/6=4

a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
op=input("Enter operator")

while(True):
if op is '+':
    if (a is 56) and (b is 9):
        print("77")
    else:
        print(a+b)

if op is '-':
    print(a-b)

if op is '*':
    if (a is 45) and (b is 3):
        print("555")
    else:
        print(a*b)

if op is '/':
    if (a is 56) and (b is 6):
        print("4")
    else:
        print(a/b)