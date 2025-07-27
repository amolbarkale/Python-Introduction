employees = [
    ("Alice", 50000, "Engineering"),
    ("Bob", 60000, "Marketing"),
    ("Carol", 55000, "Engineering"),
    ("David", 45000, "Sales")
]

# Q1] Sort by Salary

sorted_by_salary = sorted(employees, key=lambda emp: emp[1])

# Q2] Sort by Department, Then by Salary

sorted_by_dept_salary = sorted(employees, key=lambda emp: (emp[2], emp[1]))

# Q3] Create a Reversed List (without modifying original)

reversed_list = list(reversed(employees))

# Q4] Sort by Name in Reverse Order
sorted_by_name_length = sorted(employees, key=lambda emp: len(emp[0]))