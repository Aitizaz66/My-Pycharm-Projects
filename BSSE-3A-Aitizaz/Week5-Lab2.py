def calculatebill(*prices):
    tbill = 0
    for i in prices:
        tbill = tbill + i

    return tbill


def employee_info(**kwargs):
    # for i in kwargs:
    #     print(i, " : ", kwargs[i])
    print(kwargs)


def std_attendance(studentname, *days_present):
    tattendance = 0
    for i in days_present:
        if i == 'p':
            tattendance = tattendance + 1
    print("Student Name : ", studentname)
    print("Student Attendance : ", tattendance)


def place_order(*item, **detail):
    for i in item:
        print("Items Are : ", i)
    for i in detail:
        print("Detail Are : ", i, " : ", detail[i])


def report_card(name, status, **marks):
    for i in marks:
        if marks[i] > 40:
            print("Name : ", name)
            print("Status : ", status)
            print("Marks Of ", i, " : ", marks[i])


def log_transaction(**transaction):
    for i in transaction:
        print("Transaction Detail : ", i, " : ", transaction[i])


def calculate_fee(base_fee, *extras, **concessions):
    totalfee = base_fee
    for i in extras:
        totalfee = totalfee + i
    for i in concessions:
        totalfee = totalfee - concessions[i]
    print("Total Fees : ", totalfee)


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
    if choice == 1:
        print("Total Bill Is : ", calculatebill(1234, 34423, 52435, 5436346, 653634, 2342))
    elif choice == 2:
        employee_info(name="ali", age=40, department='SE', salary=100000)
        employee_info(name="ahmad", age=30, department='AI', salary=200000)
        employee_info(name="khan", age=20, department='CS', salary=150000)
    elif choice == 3:
        std_attendance("ali", "p", "p", "p", "p", "p", "p", "a", "p", "p", "a", "p", "a")
    elif choice == 4:
        place_order("chicken", "burger", "fries", "Bread", "biryani", tableno=10, waitername="ali", )
    elif choice == 5:
        report_card("ali", "pass", eng=90, math=44, urdu=35, ps=68, isl=15)
    elif choice == 6:
        log_transaction(type="withdraw", amount=50000, remarks="shop")
        log_transaction(type="add", amount=10000, remarks="online")
    elif choice == 7:
        calculate_fee(100000, 1000, 5000, 2000, 3000, 7000, 200, 500, 900, scholarships=20000)
    elif choice == 0:
        print("Exit")
        break
    else:
        print("Invalid Choice.Try Again!")
