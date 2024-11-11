# Person and Student classes (getter property)

class Person:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property #property, Python'da bir getter method'u tanımlamanın bir yoludur. Özellikle bir sınıfın bir özelliğine (attribute) dışarıdan erişildiğinde, bu özelliği bir metod gibi çağırmadan sadece bir "özellik" gibi almak isteyebilirsiniz
    def full_name(self):
        return f"{self.first} {self.last}"

    def __str__(self):
        return self.full_name


class Student(Person):

    def __init__(self, first, last, gpa):
        super().__init__(first, last)
        self.gpa = gpa

    def __str__(self):
        return f"Student: {super().__str__()}\n -- GPA: {self.gpa}"


stu1 = Student("Julia", "Smith", 3.6)
print(stu1.full_name)
print(stu1)
#week 6d full_name bir metod olarak tanımlanmış ve fonksiyon çağrısı gerektiriyordu.
# week 6e full_name bir özellik gibi davranıyor ve @property ile daha doğal bir şekilde erişilebiliyor