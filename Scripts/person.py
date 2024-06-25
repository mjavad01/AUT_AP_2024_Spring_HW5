from datetime import date
from random import randint

class ConstError(Exception):
    def __init__(self, message=" it s const do not change it!"):
        super().__init__(message)

class Person:
    def __init__(self, first_name, last_name, birthday, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.__birthday = birthday
        self.gender = gender
 
    def __new__(cls, *args, **kwargs):
        if cls is Person:
            raise TypeError("Person class not be instantiated directly")
        return object.__new__(cls)

class Student(Person):
    def __init__(self, first_name, last_name, birthday, gender, faculty, academic_degree, university, gpa=15):
        super().__init__(first_name, last_name, birthday, gender)
        if academic_degree not in ["Bachelor", "Master", "Doctoral"]:
            raise ValueError("Invalid academic degree")
        self.faculty = faculty
        self.academic_degree = academic_degree
        self.university = university
        self.gpa = gpa
        self.__student_number = ''.join([str(randint(0, 9)) for _ in range(6)])

    @property
    def student_number(self):
        return self.__student_number

    @student_number.setter
    def student_number(self, value):
        raise ConstError("Student number is immutable")

    def get_age(self):
        today = date(2024, 2, 2)
        born = self.__birthday
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

    def __str__(self):
        return f"I am {self.first_name} {self.last_name} and studying at {self.university}"

class Professor(Person):
    def __init__(self, first_name, last_name, birthday, gender, faculty, academic_rank, university, salary):
        super().__init__(first_name, last_name, birthday, gender)
        if academic_rank not in ["Professor", "Associate Professor", "Assistant Professor", "Lecturer"]:
            raise ValueError("Invalid academic rank")
        self.faculty = faculty
        self.academic_rank = academic_rank
        self.university = university
        self.__salary = salary

    def get_age(self):
        today = date.today()
        born = self.__birthday
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

    def __str__(self):
        return f"I am {self.academic_rank} {self.first_name} {self.last_name} and teaching at {self.university}"
