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
            f"ID: {self.student_id}\n"
            f"Name: {self.name}\n"
            f"Age: {self.age}\n"
            f"CGPA: {self.cgpa}\n"
            f"Department: {self.department}\n"
            f"Email: {self.email}\n"
        )

    
    def to_dict(self):
        return self.__dict__
    