

class Student:

    def __init__(self, name, major,gpa):
        self.name = name
        self.major = major
        self.gpa = gpa

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False





student1 = Student("Oscar","Accounting",3.1)
student2 = Student("Phyllis", "Business", 3.8)

print(student1.on_honor_roll())