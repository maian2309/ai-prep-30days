# students = ["Hermione", "Harry", "Ron", "Draco"]
# houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]

# print(students[0])
# print(students[1])
# print(students[2])
# print(students[3])

# for student in students:
#     print(student)

# for i in range(len(students)):
#     print(i + 1, students[i])

# students = {
#     "Hermione": "Gryffindor",
#     "Harry": "Gryffindor",
#     "Ron": "Gryffindor",
#     "Draco": "Slytherin"
# }

# print(students["Hermione"])
# print(students["Harry"])
# print(students["Ron"])
# print(students["Draco"])

# for student in students:
#     print(student, students[student], sep=", ")

students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell Terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")

# Các loại dữ liệu trong Python:
# - int: số nguyên
# - float: số thực
# - str: chuỗi ký tự
# - bool: giá trị luận lý
# - list: danh sách
# - dict: từ điển

# Ví dụ về các loại dữ liệu trong Python:
# - int: 5, 10, -3
# - float: 3.14, 2.5, -1.0
# - str: "Hello, World!", "Python"
# - bool: True, False
# - list: [1, 2, 3], ["a", "b", "c"]
# - dict: {"name": "Alice", "age": 30}