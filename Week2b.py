list1 = ["A", "B", "C", "D"]
# print(list1[3])
print(f"list1 has {len(list1)} items.")

list2 = ["Red", 17, False, "Python"]
# print(list2[0:2])
# print(list2[1:3])
# print(list2[:2])
# print(list2[2:])
# print(list2[-1])
# print(list2[-2])
# print(list2[0:-1])

list2[3] = 6
# print(list2)

list2.append("Apple")
list2.insert(3, True)
list2.remove("Red")
print(list2)

for i in list2:
    print(i)

print("\nTesting the existence of 20:")
if 20 in list2:
    print("Found.")
else:
    print("Not found.")

list3 = list2.copy()
print(list3)
