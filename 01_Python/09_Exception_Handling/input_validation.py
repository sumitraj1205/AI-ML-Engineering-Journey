while True:
    try:
        age = int(input("Enter your age: "))

        if age < 0:
            print("Age cannot be negative.")
        elif age > 120:
            print("Please enter a valid age.")
        else:
            print("Your age is:", age)
            break

    except ValueError:
        print("Please enter a valid number.")