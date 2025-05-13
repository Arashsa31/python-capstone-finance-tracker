# Function to add an expense
def add_expense(data):
    try:
        # Get expense description
        description = input("Enter expense description: ").strip()
        if not description:
            raise ValueError("Description cannot be empty.")

        # Get category
        category = input("Enter category: ").strip()
        if not category:
            raise ValueError("Category cannot be empty.")

        # Get and validate amount
        amount_input = input("Enter amount: ").strip()
        amount = float(amount_input)
        if amount < 0:
            raise ValueError("Amount cannot be negative.")

        # Add to the data dictionary
        if category not in data:
            data[category] = []
        data[category].append((description, amount))
        print("Expense added successfully.\n")
    except ValueError as ve:
        print(f"Invalid input: {ve}\n")
    except Exception as e:
        print(f"An error occurred: {e}\n")

# Function to display all expenses
def view_expenses(data):
    if not data:
        print("No expenses recorded.\n")
        return
    for category, expenses in data.items():
        print(f"Category: {category}")
        for desc, amt in expenses:
            print(f"  - {desc}: ${amt:.2f}")
    print()

# Function to display summary of expenses by category
def view_summary(data):
    if not data:
        print("No expenses to summarize.\n")
        return
    print("Summary:")
    for category, expenses in data.items():
        total = sum(amount for _, amount in expenses)
        print(f"{category}: ${total:.2f}")
    print()

# Main program loop
def main():
    print("Welcome to the Personal Finance Tracker!\n")
    data = {}  # Dictionary to store expenses

    while True:
        # Show menu options
        print("What would you like to do?")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Summary")
        print("4. Exit")
        choice = input("Choose an option: ").strip()

        # Handle menu choices
        if choice == '1':
            add_expense(data)
        elif choice == '2':
            view_expenses(data)
        elif choice == '3':
            view_summary(data)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Start the program
main()
