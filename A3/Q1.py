student = {
    "name": "Alice",
    "age": 16,
    "class": "10A"
}
print(student["name"])
print(student.get("class"))
student["age"] = 17
student["grade"] = "A"
student.pop("class")
for key, value in student.items():
    print(key, ":", value)

colors = ("red", "green", "blue")
print(colors[0])
print(len(colors))
# Tuple unpacking
r, g, b = colors
print(g)

fruits = {"apple", "banana", "cherry", "apple"}
fruits.add("orange")
fruits.discard("banana")
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))
print(set1.intersection(set2))