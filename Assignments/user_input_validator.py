

while True:
    user_input = input("Please enter your age: ")

    if not user_input:
        print("Input cannot be empty. Please try again.")
        continue

    try:
        age = int(user_input)

        if 0 <= age<= 120:
            break
        else:
            print("Age must be between 0 and 120. Please try again.")
            continue

    except ValueError:
        print("Invalid input. Please enter a valid value.")
        continue

print("Your age is:", user_input)