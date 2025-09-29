def calculatebill(*prices):
    tbill=0
    for i in prices:
        tbill=tbill+i

    return tbill
def employeeinfo(**kwargs):
    print(kwargs)

def attendance(studentname,*days_present):
    tattendance=0
    for i in days_present:
        if i=='p':
            tattendance = tattendance +1
    print("Student Name : ",studentname)
    print("Student Attendance : ",tattendance)

def place_order(*item,**detail):
    for i in item:
        print("Items Are : ",i)
    for i in detail:
        print("Detail Are : ",detail[i])
def report_card(name,status="pass",**marks):

while True:
    print("==========Menu==========")
    print("1.Calculate Store Bill")
    print("2.Employee Info")
    print("3.School Attendance")
    print("4.Place Restaurant Order")
    print("5.Student Report Card")
    print("6.Bank Transaction Logger")
    print("7.University Fee Calculator")
    print("0.Exit")
    choice = int(input("Enter Your Choice : "))
    if choice==1:
        print("Total Bill Is : ",calculatebill(1234,34423,52435,5436346,653634,2342))
    elif choice==2:
        employeeinfo(name="ali",age=40,department='SE',salary=100000)
        employeeinfo(name="ahmad", age=30, department='AI', salary=200000)
        employeeinfo(name="khan", age=20, department='CS', salary=150000)
    elif choice == 3:
        attendance("ali","p","p","p","p","p","p","a","p","p","a","p","a")
    elif choice == 4:
        place_order("chicken","burger","fries","Bread","biryani",tableno=10,waitername="ali",)
    elif choice == 5:

    elif choice == 6:

    elif choice == 7:

    elif choice == 0:
        print("Exit")
        break
    else:
        print("Invalid Choice.Try Again!")



