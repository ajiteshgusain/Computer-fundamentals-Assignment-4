# --- Calculator Functions ---

def add(x, y):
    """Adds two numbers."""
    return x + y

def subtract(x, y):
    """Subtracts two numbers."""
    return x - y

def multiply(x, y):
    """Multiplies two numbers."""
    return x * y

def divide(x, y):
    """Divides two numbers. Handles division by zero error."""
    if y == 0:
        return "Error: Cannot divide by zero"
    return x / y

# --- Main Program Loop ---

def main():
    print("Welcome to the Console Calculator!")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    
    while True:
        # Get operation choice
        choice = input("\nEnter choice (1/2/3/4/5): ")

        if choice == '5':
            print("Thank you for using the calculator. Goodbye!")
            break

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numbers only.")
                continue

            result = None
            if choice == '1':
                result = add(num1, num2)
            elif choice == '2':
                result = subtract(num1, num2)
            elif choice == '3':
                result = multiply(num1, num2)
            elif choice == '4':
                result = divide(num1, num2)
            
            print(f"\nResult: {num1} {['+', '-', 'x', '/'][int(choice)-1]} {num2} = {result}")
        
        else:
            print("Invalid Choice. Please select a valid operation (1-5).")

if __name__ == "__main__":
    main()