import csv
from datetime import datetime

# Expense class to represent an expense entry
class Expense:
    def __init__(self, amount, category, date):
        self.amount = amount
        self.category = category
        self.date = date

# Function to add a new expense
def add_expense(expenses):
    amount = float(input("Enter expense amount: "))
    category = input("Enter category (e.g., food, transport, entertainment): ").strip()
    date = input("Enter the date (YYYY-MM-DD) or leave blank for today: ").strip()
    if not date:
        date = datetime.today().strftime('%Y-%m-%d')
    expenses.append(Expense(amount, category, date))

# Function to display all expenses
def display_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
        return
    print("\nDate        | Category       | Amount")
    print("-------------------------------------")
    for expense in expenses:
        print(f"{expense.date} | {expense.category.ljust(14)} | {expense.amount:.2f}")
    print("\n")

# Function to calculate total expenses
def total_expenses(expenses):
    total = sum(expense.amount for expense in expenses)
    print(f"Total expenses: {total:.2f}")

# Function to display expenses by category
def expenses_by_category(expenses):
    category = input("Enter category to filter by: ").strip()
    filtered_expenses = [e for e in expenses if e.category == category]
    display_expenses(filtered_expenses)

# Function to export expenses to CSV
def export_to_csv(expenses, filename="expenses.csv"):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['Date', 'Category', 'Amount']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for expense in expenses:
            writer.writerow({'Date': expense.date, 'Category': expense.category, 'Amount': expense.amount})
    print(f"Expenses exported to {filename}")

def main():
    expenses = []
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add a new expense")
        print("2. View all expenses")
        print("3. View total expenses")
        print("4. View expenses by category")
        print("5. Export expenses to CSV")
        print("q. Quit")
        
        choice = input("Choose an option: ").strip()
        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            display_expenses(expenses)
        elif choice == '3':
            total_expenses(expenses)
        elif choice == '4':
            expenses_by_category(expenses)
        elif choice == '5':
            export_to_csv(expenses)
        elif choice.lower() == 'q':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
