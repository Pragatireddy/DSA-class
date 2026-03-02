expense={}
def add_expense():
    name=input("Enter the name of the expense: ")
    amount=float(input("Enter the amount of the expense: "))
    expense[name]=amount
    print("Expense added successfully!")
def view_expenses():
    if not expense:
        print("No expenses found.")
    else:
        print("Expenses:")
        for name, amount in expense.items():
            print(f"{name}: ${amount:.2f}")
def main():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
    