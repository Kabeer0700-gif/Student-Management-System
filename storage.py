import json

class Storage:
    def save_student(self,student):
        dic = student.to_dict()

        try:
            with open('students.json','w') as file:
                json.dump(dic,file)
        except FileNotFoundError:
            print("File Error")

    def load_student(self):
        try:
            with open('students.json','r') as file:
                data = json.load(file)

            return data
        
        except FileNotFoundError:
            print("file not found")
            
