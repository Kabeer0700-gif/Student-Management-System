from manager import Manager
from exception import DuplicateStudentID,InvalidCGPA,StudentNotFound
from storage import Storage
from student import Student


manager = Manager()

while True:
    print("\n================== STUDENT MANAGEMENT SYSTEM =====================")
    print("1. Add Student")
    print("2. View Student")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Sort by CGPA")
    print("7. Sort by Name")
    print("8. Count Students")
    print("9. Save Data")
    print("0. Exit")


    choice = input("Enter your choice:\t")
    match choice:
        case '1':
            id = int(input("Enter id: "))
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            department = input("Enter Department: ")
            cgpa = input("Enter CGPA: ")
            email = input("Enter email: ")
            student = Student(id,name,age,cgpa,department,email)
            manager.add_student(student)

            print("\n---------------Student Added Successfully-------------------")

        case '2':
            manager.view_student()
