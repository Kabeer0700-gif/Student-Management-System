import json

class Storage:
    def save_student(self,student):
        dic = student.to_dict()

        try:
            with open('students.json','w') as file:
                json.dump(dic,file)
        except FileNotFoundError:
            print("File Error")

