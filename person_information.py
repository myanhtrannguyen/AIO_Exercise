from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name:str, yob:int):
        self._name = name
        self._yob = yob
    def get_name(self):
        return self._name
    def get_yob(self):
        return self._yob
    @abstractmethod
    def describe(self):
        pass

class Student(Person):
    def __init__(self, name:str, yob:int, grade:str):
        super().__init__(name, yob)
        self.grade = grade

    def describe(self):
        print(f"Student - Name: {self.get_name()} - YoB: {self.get_yob()} - Grade: {self.grade}")

class Teacher(Person):
    def __init__(self, name:str, yob:int, subject:str):
        super().__init__(name, yob)
        self.subject = subject

    def describe(self):
        print(f"Teacher - Name: {self.get_name()} - YoB: {self.get_yob()} - Subject: {self.subject}")

class Doctor(Person):
    def __init__(self, name:str, yob:int, specialist:str):
        super().__init__(name, yob)
        self.specialist = specialist

    def describe(self):
        print(f"Doctor - Name: {self.get_name()} - YoB: {self.get_yob()} - Specialist: {self.specialist}")

class Ward:
    def __init__(self, name):
        self.__name = name
        self.__listPeople = list()

    def add_person(self, person):
        self.__listPeople.append(person)

    def describe(self):
        print(f"Ward Name: {self.__name}")
        for p in self.__listPeople:
            p.describe()

    def count_doctor(self):
        return len([person for person in self.__listPeople if isinstance(person, Doctor)])

    def sort_age(self):
        self.__listPeople.sort(key=lambda person: person.get_yob(), reverse=True)

    def compute_average(self):
        teachers = [person for person in self.__listPeople if isinstance(person, Teacher)]
        if not teachers:
            return 0
        return sum(person.get_yob() for person in teachers) / len(teachers)


student1 = Student(name="studentA", yob=2010, grade="7")
student1.describe()

teacher1 = Teacher(name="teacherA", yob=1969, subject="Math")
teacher1.describe()

doctor1 = Doctor(name="doctorA", yob=1945, specialist=" Endocrinologists ")
doctor1.describe()
# Create teacher and doctor
teacher2 = Teacher(name="teacherB", yob=1995, subject="History")
doctor2 = Doctor(name="doctorB", yob=1975, specialist="Cardiology")

# Create ward
ward1 = Ward(name="Ward1")

# add person to ward
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
ward1.add_person(doctor2)

# Ward description
ward1.describe()
print(ward1.count_doctor())