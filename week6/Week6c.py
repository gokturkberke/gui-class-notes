# Person class

class Person:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def full_name(self):
        return f"{self.first} {self.last}"

    def __str__(self): #full name metodunu cagirarark kisiyi tam adiyla yazdirir
        return self.full_name()


per1 = Person("James", "White")
print(per1.last) #white
print(per1.full_name()) #james white
per1.last = "Green" 
print(per1) #james green
