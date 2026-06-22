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
            print(
                f"Sno: {i+1}\n"
                f"ID: {self.students[i].student_id}\n"
                f"Name: {self.students[i].name}\n"
                f"Age: {self.students[i].age}\n"
                f"Department: {self.students[i].department}\n"
                f"CGPA: {self.students[i].cgpa}\n"
                f"Email: {self.students[i].email}\n"
            )

            print("------------------------------------------------")


    
    def search_student(self,id):
        for i,student in enumerate(self.students):
            if self.students[i].student_id == id:
                print(
                    f"ID: {self.students[i].student_id}\n"
                    f"Name: {self.students[i].name}\n"
                    f"Age: {self.students[i].age}\n"
                    f"Department: {self.students[i].department}\n"
                    f"CGPA: {self.students[i].cgpa}\n"
                    f"Email: {self.students[i].email}\n"
                )
                print("")

                break

    
    
    def delete_student(self,id):
        for i,student in enumerate(self.students):
            if self.students[i].student_id == id:
                del self.students[i]
                return True
        
        return False
    

    
    def update_student(self,id):
        name = input("Enter updated name: ")
        department = input("Enter updated department: ")
        age = input("Enter updated age: ")
        cgpa = input("Enter updated cgpa: ")
        email = input("Enter updated email: ")

        for i,student in enumerate(self.students):
            if self.students[i].student_id == id:
                self.students[i].updateName(name)
                self.students[i].updateDepartment(department)
                self.students[i].updateAge(age)
                self.students[i].updateCGPA(cgpa)
                self.students[i].updateEmail(email)

                print("Student updated with id: ",id)

                break

    
    def count_student(self):
        return len(self.students)
    



                



