a = input("Enter number 1: ")
b = input("enter number 2: ")
c = input("Enter operator: ")

if (c == "+"):
    print(int(a)+int(b))
elif (c == "-"):
    print(int(a)-int(b))
elif (c == "*" or c == "x"):
    print(int(a)*int(b))
elif (c == "/"):
    print(int(a)/int(b))
else:
    print("invalid operator")
