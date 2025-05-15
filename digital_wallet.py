expenses = []

def register_expense():
    category = input("Enter the expense category: ")
    while True:
        try:
            amount = float(input("Enter the expense amount: "))
            if amount < 0:
                print("Amount must be positive. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid amount. Please enter a valid number.")
    expenses.append({'category': category, 'amount': amount})
    print(f"Expense recorded: {category} - ${amount:.2f}")

def total_spent():
    return sum(expense['amount'] for expense in expenses)

def percentage_by_category():
    total = total_spent()
    if total == 0:
        print("No expenses recorded.")
        return
    totals_by_category = {}
    for expense in expenses:
        cat = expense['category']
        totals_by_category[cat] = totals_by_category.get(cat, 0) + expense['amount']
    print("\nPercentage spent by category:")
    for cat, amount in totals_by_category.items():
        pct = (amount / total) * 100
        print(f"{cat}: {pct:.2f}%")

def show_menu():
    print("\n--- Digital Wallet ---")
    print("1. Register expense")
    print("2. View total spent")
    print("3. View percentage by category")
    print("4. Exit")

def main():
    while True:
        show_menu()
        option = input("Select an option: ")
        if option == '1':
            register_expense()
        elif option == '2':
            print(f"Total spent: ${total_spent():.2f}")
        elif option == '3':
            percentage_by_category()
        elif option == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()