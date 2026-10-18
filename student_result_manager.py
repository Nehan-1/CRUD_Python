student = {}

while True :
    print("______Result Management System________")
    print("1. Add Students ")
    print("2. View Students ")
    print("3. Check Result")
    print("4. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter student name: ")
        marks = int(input("ENter Student marks: "))
        student[name] = marks
        print(f"{name} Successfully Added!")

    elif choice == "2":
        if not student:
            print("No student found!")
        else:
            for name,marks in student.items():
                print(name, ":" , marks)
    elif choice == "3" :
        name = input("Enter Student Name: ")

        if name in student :
            marks = student[name]

            
            print(f'student got : {marks}')
        else : print("No Student found")
    elif choice == "4" :
        print("Exiting.........")
        break
    else : 
        print("Your Choice is Wrong")



    