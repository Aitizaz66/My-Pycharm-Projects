# Functions In Python
# eval is type casting convert to float or int a=eval(input("Enter Value")
# def function_name():
#     print("Aitizaz Ahsan Awan")
#
#
# function_name()


# def add():
#     a = int(input("Enter First Number : "))
#     b = int(input("Enter Second Number : "))
#     print("Addition is ", a + b)
#
#
# def sub():
#     a = int(input("Enter First Number : "))
#     b = int(input("Enter Second Number : "))
#     print("Subtraction is ", a - b)
#
#
# def mul():
#     a = int(input("Enter First Number : "))
#     b = int(input("Enter Second Number : "))
#     print("Multiplication is ", a * b)
#
#
# def div():
#     a = int(input("Enter First Number : "))
#     b = int(input("Enter Second Number : "))
#     if b > 0:
#         print("Division is ", a / b)
#     else:
#         print("Undefined Second Number Must Be greater Than 0")
#
#
# while True:
#     print("Press 1 Addition")
#     print("Press 2 Subtraction")
#     print("Press 3 Multiplication")
#     print("Press 4 Division")
#     print("Press 5 Exit")
#     choice = int(input("Enter Your Choice : "))
#     if choice == 1:
#         add()
#     elif choice == 2:
#         sub()
#     elif choice == 3:
#         mul()
#     elif choice == 4:
#         div()
#     elif choice == 5:
#         print("Exiting Bye!")
#         break
#     else:
#         print("invalid Choice")


def add(a, b):
    print("Addition is ", a + b)


def sub(a, b):
    print("Subtraction is ", a - b)


def mul(a, b):
    print("Multiplication is ", a * b)


def div(a, b):
    if b > 0:
        print("Division is ", a / b)
    else:
        print("Undefined Second Number Must Be greater Than 0")


while True:
    print("Press + Addition")
    print("Press - Subtraction")
    print("Press * Multiplication")
    print("Press / Division")
    print("Press . Exit")
    a = eval(input("Enter Value 1 : "))
    b = eval(input("Enter Value 2 : "))
    op = input("Enter Operator : ")
    if op == '+':
        add(a, b)
    elif op == '-':
        sub(a, b)
    elif op == '*':
        mul(a, b)
    elif op == '/':
        div(a, b)
    elif op == '.':
        print("Exiting Bye!")
        break
    else:
        print("invalid Choice")

# return
# add(a,b)return (a+b)
# def add(a, b):
#     return (a + b)
