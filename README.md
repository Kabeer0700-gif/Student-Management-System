# Student Management System

A console-based Student Management System developed in Python using Object-Oriented Programming (OOP) principles. This application allows administrators to manage student records efficiently through a menu-driven interface.

## Features

* Add new students
* View all students
* Search students by ID
* Update student information
* Delete student records
* Sort students by name
* Sort students by CGPA
* Count total students
* Save data to JSON file
* Load data automatically on startup
* Custom exception handling
* Modular project structure

## Project Structure

```text
student_management_system/
│
├── main.py
├── student.py
├── manager.py
├── storage.py
├── exceptions.py
├── students.json
└── README.md
```

## Technologies Used

* Python 3
* Object-Oriented Programming (OOP)
* JSON File Handling
* Exception Handling
* Modular Programming

## Student Attributes

Each student record contains:

* Student ID
* Name
* Age
* Department
* CGPA
* Email

## Functionalities

### Add Student

Allows the administrator to create and store a new student record.

### View Students

Displays all students currently stored in the system.

### Search Student

Searches for a student using their unique Student ID.

### Update Student

Updates existing student information such as:

* Name
* Age
* Department
* CGPA
* Email

### Delete Student

Removes a student record from the system.

### Sort Students

Students can be sorted by:

* Name (Alphabetical Order)
* CGPA (Highest to Lowest)

### Count Students

Displays the total number of students in the system.

## Custom Exceptions

The project includes custom exceptions for better error handling.

### DuplicateStudentID

Raised when a student ID already exists.

### StudentNotFound

Raised when a student cannot be found.

### InvalidCGPA

Raised when CGPA is outside the valid range.

## Data Persistence

Student records are stored in a JSON file (`students.json`) to ensure data is preserved between program executions.

## How to Run

### Clone the Repository

```bash
git clone <repository-url>
```

### Navigate to Project Directory

```bash
cd student_management_system
```

### Run the Application

```bash
python main.py
```

## Example Menu

```text
===== STUDENT MANAGEMENT SYSTEM =====

1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Sort By CGPA
7. Sort By Name
8. Count Students
9. Save Data
0. Exit
```

## Future Enhancements

* Search by Department
* Email Validation
* Student Report Generation
* Logging System
* GPA Analytics Dashboard
* Database Integration (SQLite/PostgreSQL)
* GUI Version using Tkinter or PyQt
* Web Version using FastAPI and React

## Learning Outcomes

By building this project, you will gain hands-on experience with:

* Classes and Objects
* Encapsulation
* Composition
* File Handling
* JSON Serialization
* Exception Handling
* Searching and Sorting Algorithms
* Project Organization
* Git and GitHub Workflow

## Author

Muhammad Kabeer

## License

This project is developed for educational and learning purposes.
