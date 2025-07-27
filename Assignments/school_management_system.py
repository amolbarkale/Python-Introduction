school = {
    "Math": {
        "teacher": "Mr. Smith",
        "students": [("Alice", 85), ("Bob", 92), ("Carol", 78)]
    },
    "Science": {
        "teacher": "Ms. Johnson",
        "students": [("David", 88), ("Eve", 94), ("Frank", 82)]
    }
}

# 1. Print Teacher Names
for subject, info in school.items():
    print(f"{subject}: {info['teacher']}")

# 2. Calculate Class Average Grades
for subject, info in school.items():
    students = info['students']
    total = sum(grade for _, grade in students)
    avg = total / len(students)
    print(f"{subject} Average: {avg:.2f}")
