tuple1 = ("A", "B", "C")
print(tuple1) #-> ('A','B','C')
print(tuple1[0:-1])
# tuple1[0] = "X" 
#tuplelar degistirelemez!! / fakat index islemi yapilabilir
list1 = list(tuple1)
list1[0] = "X"
tuple1 = tuple(list1)
print(tuple1) #-> ('X','B','C')

i = 0
while i < len(tuple1):
    print(tuple1[i])
    i += 1
print("-- Done --")      

for x in range(5): #5 dahil degil
    print(x)    # 0 1 2 3 4
print("-- Done --")

for x in range(0, 5):
    print(x)
print("-- Done --")

for x in range(3, 10, 2):
    print(x)
print("-- Done --")
