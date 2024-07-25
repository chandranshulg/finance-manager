import json
from datetime import datetime

class PersonalFinanceManager:
    def __init__(self):
        self.transactions = []

    def add_income(self, amount, description):
        transaction = {
            'type': 'income',
            'amount': amount,
            'description': description,
            'date': datetime.now().isoformat()
        }
        self.transactions.append(transaction)

    def add_expense(self, amount, description):
        transaction = {
            'type': 'expense',
            'amount': amount,
            'description': description,
            'date': datetime.now().isoformat()
        }
        self.transactions.append(transaction)

    def view_summary(self):
        income = sum(t['amount'] for t in self.transactions if t['type'] == 'income')
        expenses = sum(t['amount'] for t in self.transactions if t['type'] == 'expense')
        balance = income - expenses

        print("\n--- Financial Summary ---")
        print(f"Total Income: ${income:.2f}")
        print(f"Total Expenses: ${expenses:.2f}")
        print(f"Balance: ${balance:.2f}")
        print("-------------------------\n")

    def save_data(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.transactions, file)

    def load_data(self, filename):
        try:
            with open(filename, 'r') as file:
                self.transactions = json.load(file)
        except FileNotFoundError:
            print(f"No data file found with the name {filename}.")

def main():
    manager = PersonalFinanceManager()

    while True:
        print("Personal Finance Manager")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Summary")
        print("4. Save Data")
        print("5. Load Data")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            amount = float(input("Enter amount: "))
            description = input("Enter description: ")
            manager.add_income(amount, description)
        elif choice == '2':
            amount = float(input("Enter amount: "))
            description = input("Enter description: ")
            manager.add_expense(amount, description)
        elif choice == '3':
            manager.view_summary()
        elif choice == '4':
            filename = input("Enter filename to save data: ")
            manager.save_data(filename)
        elif choice == '5':
            filename = input("Enter filename to load data: ")
            manager.load_data(filename)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
