class Manager:
    students = []
    count = 0

    @classmethod
    def add_student(cls,std):
        cls.count += 1
        cls.students.append(std)
        print(
            f"added student with student id: {std.student_id}"
        )

    
    @classmethod
    def view_student(cls):
        print("------------- STUDENT INFORMATION ------------------")
        for i in range(cls.count):
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




