# Functions
# ARBITRARY ARGUMENT FUNCTION USE one *  THAT N VALUES AT TIME HOW MANY ENTER YOUR THEY WILL EXCEPT IT.we didn't know that how many values will pass users.


def sum(*values):
    t_sum = 0
    print(type(values))  # tuple type
    for i in values:
        t_sum = t_sum + i
    return t_sum


print("Sum Is : ", sum(45, 46, 435, 245, 234, 234, 456, 57, 68, 67, 54, 3, 3, 2, 7, 98, 43))


def sub(*values):
    t_sub = 0
    for i in values:
        t_sub = t_sub - i
    return t_sub


print("Subtraction Is : ", sub(45, 46, 435, 245, 234, 234, 456, 57, 68, 67, 54, 3, 3, 2, 7, 98, 43))


# POSITION ARGUMENT:position matters if we define position than directly assign to parameter without position checking because we mentioned it.
def sum(val2, val1):
    return val1 + val2


print(sum(val1=34, val2=123))  # we define position here that val1=34 in function also


# ARBITRARY KEYWORDS ARGUMENTS: USE DOUBLE **
def sum(**values):
    print(type(values))  # Dictionary type store like this in memory dic={'val1':34,'val2':123} etc
    print(values["val1"])
    print(values["val2"])
    print(values['val3'])
    print(values.keys())  # print all key in the dictionary
    print(values)
    for i in values.keys():
        print(values[i])  # print all values in dic


print(sum(val1=34, val2=123, val3=234, val4=87, val5=98, val6=324))


# task user enter a value and then assign it arbitrary function
def inputfunction(**values):
    for i in values.keys():
        print("Values Are : ", values[i])


while True:
    name = input("Enter Name (or '0' to stop): ")
    if name == "0":
        break
    age = int(input("Enter Age: "))

    # Call function with dynamic values
    inputfunction(Name=name, Age=age)
