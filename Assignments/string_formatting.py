# Variables
name = "Amol"
age = 25
city = "Pune"

# 1. % formatting (old style)
print("1. %% formatting:")
print("Hello, my name is %s. I am %d years old and I live in %s." % (name, age, city))

# 2. .format() method
print("Hello, my name is {}. I am {} years old and I live in {}.".format(name, age, city))

# 3. f-strings (modern, Python 3.6+)
print(f"Hello, my name is {name}. I am {age} years old and I live in {city}.")
