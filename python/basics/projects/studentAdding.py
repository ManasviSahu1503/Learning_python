class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print("Name:",self.name)
        print("Roll No:",self.roll_no)
        print("Marks:",self.marks)

student1 = Student("Samarth",101,85)
student2= Student("Devansh",102,78)

print("Student 1")
student1.display()

print("Student 2")
student2.display()