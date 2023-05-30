from abc import ABCMeta, abstractstaticmethod

class IPerson(metaclass=ABCMeta):
    
    @abstractstaticmethod
    def person_method():
        print("creandose")
        """ interface method : basicamente definicion de la firma de, solo sabemos que todos las personas tienen que implementar ese metodo pero no como"""
        
        

class Student(IPerson):
    
    def __init__(self,name):
        self.name = name
        
    def person_method(self):
        print("i am a student" + self.name)
        
        
class Teacher(IPerson):
    
    def __init__(self):
        self.name = "andres"
        
    def person_method(self):
        print("i am a teacher")


class PersonFactory:
    
    @staticmethod
    def build_person(person_type,persona):
        if person_type == "Student":
            return Student(persona)
        if person_type == "Teacher":
            return Teacher()
        else:
            print("invalid type")
            return -1
        
        

if __name__ == "__main__":
    choice = input("what type of person you want to create \n")
    persona = input("name \n")

    person = PersonFactory.build_person(choice,persona)
    person.person_method()