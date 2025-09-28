# a=str(input("Enter String : "))
# #for string for loop print one character at a time
# count=0
# for i in a:
#     if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
#         print("Vowels are : "+ i)
#         count=count+1
#     #else:
#     #   print("Consonant : "+i)
#
#
# print("Vowels Count is : ",count)


#task 2 create list [] using for loop enter 5 student detail id name cgpa semester address print list.
students=[]
for i in range(1) :
    print("\nEnter details for Student :",i+1)
    sid=int(input("Enter Student Id: "))
    name=str(input("Enter Student Name : "))
    cgpa=float(input("Enter Cgpa : "))
    semester=int(input("Enter Semester : "))
    address=str(input("Enter Address : "))
    student=[sid,name,cgpa,semester,address]
    students.append(student)

print("\nAll Student Data:")
for i in students:
    print(i)


