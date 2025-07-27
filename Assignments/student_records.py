students = [
    (101, "Alice", 85, 20),
    (102, "Bob", 92, 19),
    (103, "Carol", 78, 21),
    (104, "David", 88, 20)
]

# 1. Find the Student with the Highest Grade

top_student = max(students, key=lambda student: student[2])
print("Top Student:", top_student)

# 2 Create a Name-Grade List
name_grade_list = []

for student in students:
    name = student[1]
    grade = student[2]
    name_grade_list.append((name, grade))
print("Name-Grade List:", name_grade_list)