grades = [85, 92, 78, 90, 88, 76, 94, 89, 87, 91]

# 1] Slice grades from index 2 to 7

sliced_graes = grades[2:7]

# 2] Use list comprehension to find grades above 85

abpve_85 = [grade for grade in grades if grade > 85]

# 3] Replace the grade at index 3 with 95

grades[3] = 95

# 4] Append three new grades

grades.extend([92,90,55])

# 5] Sort in descending order and display the top 5 grades

grades.sort(reverse=True)
top_five_grades = grades[:5]