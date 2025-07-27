fruits_list = ["apple", "banana", "orange", "apple", "grape"]
fruits_tuple = ("apple", "banana", "orange")
fruits_set = {"apple", "banana", "orange", "grape"}
fruits_dict = {"apple": 5, "banana": 3, "orange": 8, "grape": 2}

# 1. Check for Membership
print("apple" in fruits_list)   
print("apple" in fruits_tuple)  
print("apple" in fruits_set)    
print("apple" in fruits_dict) 

# 2. Find Length

print("List length:", len(fruits_list))     
print("Tuple length:", len(fruits_tuple))   
print("Set length:", len(fruits_set))       
print("Dict length:", len(fruits_dict))

#  3. Iterate and Print Elements

# List
for item in fruits_list:
    print(item)

# Tuple
for item in fruits_tuple:
    print(item)

# Set
for item in fruits_set:
    print(item)

# Dict
for key, value in fruits_dict.items():
    print(f"{key}: {value}")

# 4. Compare Membership Testing Performance
# Fastest: set and dict (average O(1) time)
# Slower: list and tuple (linear O(n) time)

# set and dict use hash tables internally.
# list and tuple check membership by scanning through elements one by one.
