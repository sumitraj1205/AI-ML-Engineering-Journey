try:
    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))

    result = number1 / number2

    print("Result:", result)

except ValueError:
    print("Please enter numbers only.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

finally:
    print("Program completed.")