from manager import Manager
from storage import Storage
from student import Student
from exception import DuplicateStudentID,StudentNotFound,InvalidCGPA,InvalidEmail


manager = Manager()
data = Storage.load_student()
for student_data in data:
    student = Student.from_dict(student_data)
    manager.students.append(student)

while True:
    print("\n=================== STUDENT MANAGEMENT SYSTEM ======================")
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
            age = int(input("Enter Age: "))
            department = input("Enter Department: ")
            cgpa = float(input("Enter CGPA: "))
            email = input("Enter email: ")

            try:
                student = Student(id,name,age,cgpa,department,email)
                manager.add_student(student)
                print("\n--------------- Student Added Successfully -------------------")

            except InvalidCGPA as e:
                print(e)

            except InvalidEmail as e:
                print(e)

            except DuplicateStudentID as e:
                print(e)


        case '2':
            manager.view_student()

        case '3':
            id = int(input("\nEnter id: "))
            try:
                 student = manager.search_student(id)
                 student.display()
            except StudentNotFound as e:
                  print(e)
            
        case '4':
            id = int(input("\nEnter id: "))
            student = manager.search_student(id)
            if student:
                name = input("Enter new name: ")
                age = int(input("Enter new age: "))
                department = input("Enter new department: ")
                email = input("Enter new email: ")
                cgpa = float(input("Enter new cgpa: "))
                manager.update_student(student,name,department,age,cgpa,email)
                print(f"\nstudent with id {id} updated successfully")
            else:
                print("No Student found with id: ",id)

        case '5':
            id = int(input("\nEnter id:"))
            check = manager.delete_student(id)
            if check:
                print(f"Student with id : {id} Deleted Successfully")
            else:
                print(f"Student with id:{id} Not FOund")

        case '6':
            sorted_students_cgpa = manager.sort_by_cgpa()
            print("\n------------------- Student with Highest CGPA ----------------------\n")
            if sorted_students_cgpa:
                for student in sorted_students_cgpa:
                    student.display()
            else:
                print("Student Not Added Yet !!!")


        case '7':
            sorted_students_name = manager.sort_by_name()
            print("\n------------------- Student in Alphabatical Order ----------------------\n")
            if sorted_students_name:
                for student in sorted_students_name:
                    student.display()
            else:
                print("Student Not Added Yet !!!")

        case '8':
            count_student = manager.count_student()
            if count_student == 0:
                print("OOPs no student added yet !!")
            else:
                print(f"Total Student: {count_student}")

        case '9':
            Storage.save_student(manager.students)
            print("Data saved successfully!")

        case '0':
            Storage.save_student(manager.students)
            print("Data saved. Exiting...")
            break
        