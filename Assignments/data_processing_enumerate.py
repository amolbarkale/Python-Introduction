# You are given two lists containing student names and their corresponding scores:

students = ["Alice", "Bob", "Charlie", "David"]
scores = [85, 92, 78, 90]

# Q1] Print each student’s name with a number starting from 1 (e.g., 1. Alice).

# i = 1
# for stud in students:
#     print(f"Student {i}: {stud}, score: {scores[i-1]}")

for i, name in enumerate(students, start=1):
    print(f"Student {i}: {name}")
# _____________________________________________________________________________

# Q2] Combine both lists to display each student's name alongside their score.

for name, score in zip(students, scores):
    print(f"{name} scored {score}")
# _____________________________________________________________________________

# Q3] Identify and print the positions (indices) of students who scored above 90.

for index, score in enumerate(scores):
    if score > 90:
        print(f"Student at index {index} scored above 90: {students[index]} with score {score}")

# Q] Create a dictionary where keys are positions (starting from 0) and values are the student names.

student_dict = {index: name for index, name in enumerate(students)}

