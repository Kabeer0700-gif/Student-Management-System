class Manager:
    
    def __init__(self):
        self.students = []

    def add_student(self,std):
        self.students.append(std)
        print(
            f"added student with student id: {std.student_id}"
        )

    
    
    def view_student(self):
        print("------------- STUDENT INFORMATION ------------------")
        for i,student in enumerate(self.students):
            print(f"Sno:{i+1}")
            student.display()

            print("------------------------------------------------")


    
    def search_student(self,id):
        for student in self.students:
            if student.student_id == id:
                student.display()
                print("")

                break

    
    
    def delete_student(self,id):
        for student in self.students:
            if student.student_id == id:
                self.students.remove(student)
                return True
        
        return False
    

    
    def update_student(self,id,name,department,age,cgpa,email):
        for student in self.students:
            if  student.student_id == id:
                student.updateName(name)
                student.updateDepartment(department)
                student.updateAge(age)
                student.updateCGPA(cgpa)
                student.updateEmail(email)

                print("Student updated with id: ",id)

                break

    
    def count_student(self):
        return len(self.students)
    
    def sort_by_cgpa(self):
        sorted_students = sorted(
            self.students,
            key = lambda student:student.cgpa,
            reverse=True
        )
        print("-------------- Students with highest cgpa ----------------")
        for student in sorted_students:
            print(
                f"{student.name}\t{student.cgpa}"
            )


    def sort_by_name(self):
        sorted_students = sorted(
            self.students,
            key = lambda student:student.name
        )

        print("-------------- Students in Alphabatecal Order ----------------")
        for student in sorted_students:
            print(
                f"{student.name}\t{student.cgpa}"
            )



    



                



