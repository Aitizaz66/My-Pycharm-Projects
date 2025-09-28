studentlist = []
while True:
    print("Press 1 To Enter New Student Record")
    print("Press 2 To Show Data OF All Student ")
    print("Press 3 To Search By ID")
    print("Press 4 To Search By Name")
    print("Press 5 To Remove Student By Id")
    print("Press 6 To Exit")
    choice = int(input("Enter Your Choice : "))
    if choice == 1:
        print("Enter New Student Data : ")
        name = input("Enter Student Name: ")
        sid = int(input("Enter Student Id : "))
        age = int(input("Enter Age OF Student "))
        student = {
            'id': sid,
            'Student Name': name,
            'Age': age
        }
        studentlist.append(student)
    elif choice == 2:
        if not studentlist:
            print("No Student Found")
        else:
            for student in studentlist:
                print(student)
    elif choice == 3:
        sid = int(input("Enter ID To Search : "))
        found = False
        for student in studentlist:
            if student['id'] == sid:
                print("student data : ", student)
                found = True
                break
        if not found:
            print("Not Found")

    elif choice == 4:
        name = input("Enter Name To Search : ")
        found = False
        for student in studentlist:
            if student['Student Name'].lower() == name.lower():
                print("student data : ", student)
                found = True
                break
        if not found:
            print("Not Found")
    elif choice == 5:
        sid = int(input("Enter Student Id To Delete Student Record : "))
        found = False
        for student in studentlist:
            if student['id'] == sid:
                studentlist.remove(student)
                print("Deleted")
                found = True
                break
        if not found:
            print("Not Found")
    elif choice == 6:
        print("Bye")
        break
    else:
        print("invalid Choice")
