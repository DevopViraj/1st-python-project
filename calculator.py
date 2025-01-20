def calculator():
    while True:
        numbers = []
        while True:
            a = input("Enter a number (or 'done' to finish): ")
            if a == "done":
                break
            try:
                a = int(a)
                numbers.append(a)
            except ValueError:
                print("That's not a valid number or 'done' to finish.")

        if not numbers:
            print("No numbers provided")
            exit()

        operation = input('''Thanks for the numbers! Now please select from below options which type of operation you want to perform:
 1 for Addition
 2 for Subtraction
 3 for Multiplication
 4 for Division
 5 for exit
 Enter your choice: ''')

        if operation == '1':
            total_sum = sum(numbers)
            print(f"Sum of your given numbers is {total_sum}")

        elif operation == '2':
            # Check if the list has at least one number
            if len(numbers) > 0:
                answer = numbers[0]  # Start with the first number
                for num in numbers[1:]:  # Subtracting remaining numbers
                    answer -= num
                print(f"Subtraction of your given numbers is {answer}")
            else:
                print("No numbers provided for subtraction")

        elif operation == '3':
            total_product = 1
            for num in numbers:
                total_product *= num
            print(f"Multiplication of your given numbers is {total_product}")

        elif operation == '4':
            # Check if the list has at least one number
            if 0 in numbers[1:]:
                print("Division by zero is not allowed")
            elif len(numbers) > 0:
                answer = numbers[0]  # Start with the first number
                for num in numbers[1:]:
                    answer /= num
                print(f"Division of your given numbers is {answer}")
            else:
                print("No numbers provided for division")

        elif operation == '5':
            print("Exiting the calculator..")
            exit()

        else:
            print("Invalid choice")

        # Asking the user for further continuation of the program
        repeat = input("Do you want to perform further operations? (yes/no): ")
        if repeat.lower() != 'yes':
            print("Exiting the calculator..")
            exit()

calculator()

