product_name = "Pen"
price = 5
available = True #urunun mevcut olup olmadigini belirtiyo

print(product_name + " $" + str(price) + ".")
print(f"{product_name} ${price}.")

# age = int(input("Enter your age: "))
# age += 1
# print(age)

a = b = c = "Hey" #3u de hey degerini alir
d, e, f = 3, "A", False #sirasiyla deger alirlar

print(a, b, c) 
print(d, e, f)
print(type(d))

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

if num1 > num2:
    print(f"{num1} is greater than {num2}.")
    print("-- First condition --")
elif num2 > num1:
    print(f"{num2} is greater than {num1}.")
    print("-- Second condition --")
else:
    print("Numbers are equal.")
    print("-- Third condition --")

# and or
