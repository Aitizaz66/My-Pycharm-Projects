#Dictionaries
# Denoted By {}.It's A Data Structure
# id name and age are Keys
# d1={'id':1,
#     'Name':"Ali",
#     'Age': 20
#     }
# print(d1.keys())
# print(d1.values())
# print(d1.copy())


#Loop
# While Loop
# num=10
# while num!=0:
#     print(num)
#     num=num-1

# FOR Loop
# print(range(10))#show range from 0 to 10 10 not include
# for i in range(2,20,2):#First no Include. And 2nd Not Include.And 3 one is i++ mean anything + with 2 by default is 1.
#     print(i)
# print('New Loop')
# for i in range(20, 2, -3):#20 include 2 not include and -3 is i-3
#     print(i)

#list Example
# l1=[i for i in range(5,51,5)]#when executd
# print(l1)
# print("even * 10")
# l1=[i*10 for i in range(5,51,5) if i%2==0]#i*10 is basically return in python in list and store in list %2==0 return only even
# print(l1)




# Check Number is ArmStrong or Not
#
# num= int(input('Enter Number: '))
# num1=str(num)
# count= len(num1)
# print(count)
# num2=num%2
# print(num2)


# Check Number is Armstrong or Not

num = int(input("Enter Number: "))

# Step 1: Convert number to string to count digits
num_str = str(num)
count = len(num_str)

# Step 2: Calculate sum of digits raised to the power of count
sum_of_powers = 0
for digit in num_str:
    sum_of_powers += int(digit) ** count

# Step 3: Check Armstrong condition
if sum_of_powers == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is NOT an Armstrong number")
