import json

class Storage:
    @staticmethod
    def save_student(students):
        data = [
             student.to_dict()
             for student in students
        ]
        with open('students.json','w') as file:
                json.dump(data,file,indent=4)
        
    @staticmethod
    def load_student():
        try:
            with open('students.json','r') as file:
                data = json.load(file)

            return data
        
        except FileNotFoundError:
            return []

