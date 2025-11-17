def hasham():
    # This is a Number guessing game which prompts the user to enter the 
    # guess value and randomly generates a number between 1 and 50. Then
    # compares the number with guess value and if it's equal then it
    # congratulates the user otherwise prompts the user to enter the guess
    # alongwith hints
 
    # importing library for random function
    import random

    print("---------Welcome to Number guessing game---------")
    choice = "Y"

    while(choice == "Y"):
        # Generating random number between 1 and 50
        targetNumber = random.randint(1,50)
        # Initializing tries to 1
        tries = 1
        #Prompting user to enter the guess
        guessNumber = int(input(f"Enter your guess {tries}(between 1 and 50): "))

        # if guess is not valid then prompting the user again
        while (guessNumber < 0) or (guessNumber> 50):
            guessNumber = int(input(f"Invalid guess entered.Enter your guess {tries}: "))

        # if guess is not equal to target number prompting the user again along with some hints
        while guessNumber!=targetNumber:
            if guessNumber>targetNumber :
                   print("Entered number is greater than the target number.")
            else :
                 print("Entered number is less than the target number.")
            # Incrementing the tries by 1
            tries +=1
            # Again prompting the user to enter guess
            guessNumber = int(input(f"Enter your guess {tries}(between 1 and 50): "))
            while (guessNumber < 0) or (guessNumber> 50): 
                guessNumber = int(input(f"Try again.Enter your guess{tries}: "))

        # Congratulating the player and displaying in how many tries he guessed the number
        print(f"Congratulations. You guessed the right number in {tries} tries.")
        # Asking the user whether he wants to play again
        choice = input("Do you want to play again(Y/N):").upper()
        while choice!="Y" and choice != "N": 
            choice = input(f"Invalid choice. Do you want to play again(Y/N): ").upper()

    print("Thank you for playing.")
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
