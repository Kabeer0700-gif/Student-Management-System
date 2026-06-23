from exception import DuplicateStudentID,StudentNotFound,InvalidCGPA
class Manager:
    
    def __init__(self):
        self.students = []

    def add_student(self,student):
        for std in self.students:
            if std.student_id == student.student_id:

                raise DuplicateStudentID (
                    f"Student with id:{student.student_id} already exist"
                )
            
        self.students.append(student)
        print(
            f"added student with student id: {student.student_id}"
        )

    
    
    def view_student(self):
        print("------------- STUDENT INFORMATION ------------------")
        for i,student in enumerate(self.students):
            print(f"Sno:{i+1}")
            student.display()

            print("------------------------------------------------")


    def get_student(self,id):
        for student in self.students:
            if student.student_id == id:
                return student
        
        return None

    def search_student(self,id):
        student = self.get_student(id)
        if student:
            return student
        else:
            return None
            

    
    
    def delete_student(self,id):
        student = self.get_student(id)
        if student:
            self.students.remove(student)
            return True
        
        return False
    

    
    def update_student(self,student,name,department,age,cgpa,email):
        student.updateName(name)
        student.updateDepartment(department)
        student.updateAge(age)
        student.updateCGPA(cgpa)
        student.updateEmail(email)


    def count_student(self):
        return len(self.students)
    
    def sort_by_cgpa(self):
        if self.count_student() != 0:
            sorted_students = sorted(
                self.students,
                key = lambda student:student.cgpa,
                reverse=True
            )
            
            return sorted_students
        else:
            return None


    def sort_by_name(self):
        if self.count_student() != 0:
            sorted_students = sorted(
                self.students,
                key = lambda student:student.name
            )

            return sorted_students

        else:
            return None
