class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    
    def check_results(self):
        if self.marks > 50:
            print(True)
        else:
            print(False)

if __name__ == "__main__":
    student1 = Student("Anjan",30)
    student2 = Student("Vinay",70)
    student1.check_results()
    student2.check_results()