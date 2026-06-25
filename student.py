from exception import InvalidCGPA
class Student:
    def __init__(self,student_id,name,age,cgpa,department,email):
        if not  0<= cgpa <=4:
            raise InvalidCGPA(
                "CGPA must be between 0 and 4"
            )
        self.student_id = student_id
        self.name = name
        self.age = age
        self.cgpa = float(cgpa)
        self.department = department
        self.email = email

    def updateName(self,newName):
        self.name = newName

    def updateDepartment(self,newDept):
        self.department = newDept

    def updateAge(self,newAge):
        self.age = newAge

    def updateCGPA(self,cgpa):
        self.cgpa = cgpa

    def updateEmail(self,newEmail):
        self.email = newEmail
        
    def display(self):
        print(
            f"ID: {self.student_id}\n"
            f"Name: {self.name}\n"
            f"Age: {self.age}\n"
            f"CGPA: {self.cgpa}\n"
            f"Department: {self.department}\n"
            f"Email: {self.email}\n"
        )

    
    def to_dict(self):
        return {
            "student_id":self.student_id,
            "name":self.name,
            "age":self.age,
            "department":self.department,
            "cgpa":self.cgpa,
            "email":self.email
        }
    

    @classmethod
    def from_dict(cls,data):
        return cls(
            data['student_id'],
            data['name'],
            data['age'],
            data['cgpa'],
            data['department'],
            data['email'],
        )