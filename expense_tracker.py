# Simple Expense Tracker
# Beginner-friendly project using lists and file handling

FILENAME = "expenses.txt"


def load_expenses():
    expenses = []
    try:
        with open(FILENAME, "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    name, amount = line.split(",")
                    expenses.append((name, float(amount)))
    except FileNotFoundError:
        pass  # File will be created when saving
    return expenses


def save_expenses(expenses):
    with open(FILENAME, "w") as file:
        for name, amount in expenses:
            file.write(f"{name},{amount}\n")


def add_expense(expenses):
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))
    expenses.append((name, amount))
    save_expenses(expenses)
    print("Expense added!\n")


def view_expenses(expenses):
    if not expenses:
        print("No expenses found.\n")
        return

    print("\n--- Your Expenses ---")
    for i, (name, amount) in enumerate(expenses, start=1):
        print(f"{i}. {name} - ₹{amount}")
    print()


def show_total(expenses):
    total = sum(amount for _, amount in expenses)
    print(f"Total spending: ₹{total}\n")


def main():
    expenses = load_expenses()

    while True:
        print("===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Total Spending")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            show_total(expenses)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.\n")


if __name__ == "__main__":
    main()
