a = int(input("Enter number 1: "))
b = int(input("enter number 2: "))
c = input("Enter operator: ")

if (c == "+"):
    print(a + b)
elif (c == "-"):
    print(a - b)
elif (c == "*" or c == "x"):
    print(a * b)
elif (c == "/"):
    if (b == 0):
        print("undefined- division by 0")
    else:
        print(a / b)
else:
    print("invalid operator")