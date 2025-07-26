
# 1] Conventional For loop
arr1 = []
for i in range(10):
    arr.append(i)

# 2] Comprehensive For loop
arr2 = [item for item in range(10)]

# ____________________________________________________________________ #
# 3] Conventional Filtering
arr3 = []

for i in range(10):
    if(i%2 == 0):
        arr3.append(i)

# 4] Comprehensive Filtering
arr4 = [item for item in range(10) if item % 2 == 0]
# ____________________________________________________________________ #

# 5] Conventional Nested For loop
arr5 = []

for i in range(10):
    for j in range(5):
        arr5.append((i, j))

# 6] Comprehensive Nested For loop
arr6 = [(i, j) for i in range(10) for j in range(5)]
