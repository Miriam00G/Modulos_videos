class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello! I am a person.")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def greet(self):
        super().greet()
        print(f"Hi, I'm {self.name}, and I'm a student with ID: {self.student_id}")

# Crear instancia de Student y llamar a greet
student = Student("Miryam", 20, "S12345")
student.greet()  