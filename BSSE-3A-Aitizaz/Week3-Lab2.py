while True:
    print("Press 1 To Enter New Student Record")
    print("Press 2 To Show Data OF All Student ")
    print("Press 3 To Search By Nam")
    print("Press 4 To Remove Student By Id")
    print("Press 5 To Exit")
    choice = int(input("Enter Your Choice : "))
    if choice == 1:
        print("Enter New Student Data : ")
        sname = input("Enter Student Name: ")
        sid = int(input("Enter Student Id : "))
        tmarks = input("Enter Total Marks : ")
        obmarks = input("Enter Obtained Marks : ")
        disp = input("Enter Discipline : ")
        grade = input("Enter Grade : ")

    elif choice == 2:
        id = input("Enter Student Id To Show Data : ")



    elif choice == 3:
        name = input("Enter Name To Search : ")



    elif choice == 4:
        id = input("Enter Student Id To Delete Student Record")

    else:
        print("invalid Choice")
