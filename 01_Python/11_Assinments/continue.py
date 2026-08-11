while(True):
    b = input("enter the value")
    if b.lower() == "quit":
        print("stoping the program")
        break
    try:
        num = float(b)

        if num > 0:
            print("Positive number")
        elif num < 0:
            print("Negative number")
        else:
            print("Zero")

    except ValueError:
        print("Invalid input! Please enter a valid number.")