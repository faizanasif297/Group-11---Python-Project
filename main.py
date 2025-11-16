    # Arithmetic Calculator
# This program allows the user to perform basic arithmetic
# operations (+, -, *, /) on two numbers
# It includes simple exception handling to prevent crashes

def faizan():
    print("---------Arithmetic Calculator---------")

    while True:  # Outer loop for repeating calculations until user wants to stop
        # Loop until valid numbers are entered by the user
        while True:
            print("Please enter the two numbers to perform calculations.")
            # Exception handling for the right input by the user
            try:
                a = float(input("Enter the first number: "))
                b = float(input("Enter the second number: "))
                break  # Exit loop if input is valid
            except ValueError:
                print("Invalid input! Please enter numbers only.")
        # Seperate Loop for operations to not try operations if user entered wrong input
        # Loop until a valid operation is entered
        while True:
            op = input("Enter the operation (+, -, *, /) or -1 to exit: ")
            if op == "-1":
                print("Exiting calculator. Goodbye!")
                break  # Exit operation loop and go to outer loop and check exit conditions
            elif op == "+":
                print("Result:", a + b)
                break
            elif op == "-":
                print("Result:", a - b)
                break
            elif op == "*":
                print("Result:", a * b)
                break
            elif op == "/":
                if b == 0:
                    print("Error: Cannot divide by zero! Please enter numbers again.")
                    break  # Breaks to outer loop to re-enter numbers
                else:
                    print("Result:", a / b)
                    break
            else:
                print("Invalid operation! Please choose +, -, *, /, or -1 to exit.")

        # Check if the input was -1 after inner loop to exit the outer loop
        if op == "-1":
            break  # Exit outer loop to exit the calculator
