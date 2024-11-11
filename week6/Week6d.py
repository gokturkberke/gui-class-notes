# Person and Student classes (Inheritance)

class Person:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def full_name(self):
        return f"{self.first} {self.last}"

    def __str__(self):
        return self.full_name()


class Student(Person): #inheritance student sinifinin person sinifinin tum ozellikleri ve metodlarini alir

    def __init__(self, first, last, gpa):
        super().__init__(first, last) #super kodu  miras alınan (inheritance) sınıfın __init__ metodunu çağırmak için kullanılır. 
        self.gpa = gpa #gpa parametresi ekledik

    def __str__(self):
        return f"Student: {super().__str__()}\n -- GPA: {self.gpa}"


stu1 = Student("Julia", "Smith", 3.6)
print(stu1)
