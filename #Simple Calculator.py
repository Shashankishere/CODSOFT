#Simple Calculator

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero is not allowed."
    else:
        return x / y

def calculator():
    print("Welcome to Simple Calculator!")
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print("Operations:")
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")
            choice = input("Enter choice (1/2/3/4): ")

            if choice in ['1', '2', '3', '4']:
                if choice == '1':
                    print("Result:", add(num1, num2))
                elif choice == '2':
                    print("Result:", subtract(num1, num2))
                elif choice == '3':
                    print("Result:", multiply(num1, num2))
                elif choice == '4':
                    print("Result:", divide(num1, num2))
            else:
                print("Invalid choice! Please enter 1, 2, 3, or 4.")

            another_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
            if another_calculation != 'yes':
                print("Thank you for using Calculator!")
                break
        except ValueError:
            print("Invalid input! Please enter numeric values.")

calculator()
