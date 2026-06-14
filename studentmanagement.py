students = []
def add_student():
    name = input("Enter your name")
    roll = input("Enter your roll number")
    marks = input("Enter your marks")


    student = {
    "Name": name,
    "Roll": roll,
    "Marks": marks}
     

    students.append(student)
    print("Student added succesfully ")
    
def view_students():
    if len(students) == 0:
        print("No student found")
    else:
        print("Student list")

        for s in students:
            print("-------------")
            print ("Name:", s["Name"])
            print ("Roll:", s["Roll"])
            print ("Marks:", s["Marks"])
        print()

def search_student():
    roll = input("Enter roll number to search: ")

    for s in students:
        if s["Roll"] == roll:
            print("\nStudent Found")
            print("Name :", s["Name"])
            print("Roll :", s["Roll"])
            print("Marks:", s["Marks"])
            print()
            return

    print("Student not found.\n")


# Function to delete student
def delete_student():
    roll = input("Enter roll number to delete: ")

    for s in students:
        if s["Roll"] == roll:
            students.remove(s)
            print("Student deleted successfully!\n")
            return

    print("Student not found.\n")



while True:
    print("====Student Management System")
    print("1.Add student")
    print("2.view student")
    print("3.search student")
    print("4.delete student")
    print("5.exit")

        
    choice = input("Enter your choice:")

    if choice == "1":
        add_student()

    elif choice == "2":
       view_students()

    elif choice == "3":
        search_student()
    elif choice == "4":
       delete_student()
    else:
        break

    
        




        

