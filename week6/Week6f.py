# Person and Student classes (setter property)

class Person:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property #@property dekoratörüyle full_name bir özellik (attribute) gibi davranır. Bu, dışarıdan full_name'a fonksiyon çağrısı yapmadan erişilmesini sağlar.
    def full_name(self): 
        return f"{self.first} {self.last}"

    @full_name.setter #@full_name.setter dekoratörü, full_name'a bir değer atandığında çalışan metodu belirtir. Bu metod, verilen tam ismi (örneğin "Olivia Ross") ikiye ayırarak, first ve last isimlerini ayrı ayrı atar.
    def full_name(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    def __str__(self):
        return self.full_name


class Student(Person):

    def __init__(self, first, last, gpa):
        super().__init__(first, last)
        self.gpa = gpa

    def __str__(self):
        return f"Student: {super().__str__()}\n -- GPA: {self.gpa}"


stu1 = Student("Julia", "Smith", 3.6)
stu1.full_name = "Olivia Ross"
print(stu1)

#full_name.setter olmasa deger atayamazdik
# setter fonksiyonu olmadan full_name'a değer atamak mümkün değildir, ancak doğrudan first ve last'ı değiştirebilirsiniz. Setter fonksiyonu, full_name üzerinden ismi güncellemeyi sağlar.