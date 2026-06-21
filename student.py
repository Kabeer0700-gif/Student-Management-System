class Student:
    def __init__(self,student_id,name,age,cgpa,department,email):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.cgpa = cgpa
        self.department = department
        self.email = email

    def display(self):
        print(
            "\n-----------------Student Information---------------------\n"
            f"ID: {self.student_id}"
            f"Name: {self.name}"
            f"Age: {self.age}"
            f"CGPA: {self.cgpa}"
            f"Department: {self.department}"
            f"Email: {self.email}"
        )
        