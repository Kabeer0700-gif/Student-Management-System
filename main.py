from manager import Manager
from exception import DuplicateStudentID,InvalidCGPA,StudentNotFound
from storage import Storage
from student import Student


while True:
    print("================== STUDENT MANAGEMENT SYSTEM =====================")
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

    