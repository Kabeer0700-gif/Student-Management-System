class Manager:
    students = []
    @classmethod
    def add_student(cls,std):
        cls.students.append(std)
        print(
            f"added student with student id: {std.student_id}"
        )

    
    @classmethod
    def view_student(cls):
        print("------------- STUDENT INFORMATION ------------------")
        for i,student in enumerate(cls.students):
            print(
                f"Sno: {i+1}\n"
                f"ID: {cls.students[i].student_id}\n"
                f"Name: {cls.students[i].name}\n"
                f"Age: {cls.students[i].age}\n"
                f"Department: {cls.students[i].department}\n"
                f"CGPA: {cls.students[i].cgpa}\n"
                f"Email: {cls.students[i].email}\n"
            )

            print("------------------------------------------------")


    @classmethod
    def search_student(cls,id):
        for i,student in enumerate(cls.students):
            if cls.students[i].student_id == id:
                print(
                    f"ID: {cls.students[i].student_id}\n"
                    f"Name: {cls.students[i].name}\n"
                    f"Age: {cls.students[i].age}\n"
                    f"Department: {cls.students[i].department}\n"
                    f"CGPA: {cls.students[i].cgpa}\n"
                    f"Email: {cls.students[i].email}\n"
                )
                print("")

                break

    
    @classmethod
    def delete_student(cls,id):
        for i,student in enumerate(cls.students):
            if cls.students[i].student_id == id:
                del cls.students[i]
                return True
        
        return False
    

                



