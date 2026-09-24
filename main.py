import json
from datetime import datetime
file_name="expenses.json"

def load_expenses():
    try:
        with open(file_name,"r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecoderError:
        return[]

def save_expenses(expenses):
    with open(file_name,"w") as file:
        json.dump(expenses,file,indent=4)

def add_expense(expenses):
    category=input("Category : ").strip()
    try:
        amount=float(input("Amount : "))
    except ValueError:
        print("Please Enter A Valid Amount!")
    description=input("Description : ").strip()
    date=datetime.now().strftime("%Y-%m-%d")
    expense={
        "id":len(expenses)+1,
        "category":category,
        "amount":amount,
        "date":date,
        "description":description
    }
    expenses.append(expense)
    save_expenses(expenses)
    print("Expense Added Successfully.")

def view_expenses(expenses):
    if not expenses:
        print("No Expenses in found !")
    for expense in expenses:
        print(
            f"ID: {expense['id']}\n"
            f"Date:{expense['date']}\n"
            f"Category:{expense['category']}\n"
            f"Amount:{expense['amount']:.2f}\n"
            f"Description:{expense['description']}\n---------------"
        )

def calculate_total(expenses):
    total = sum(expense["amount"] for expense in expenses)
    print(f"Total expenses: {total:.2f}")

def search_expenses(expenses):
    keyword=input("Search : ").lower()
    results=[
        expense for expense in expenses
        if keyword in expense["category"].lower()
        or keyword in expense["description"].lower()
    ]
    view_expenses(results)

def delete_expense(expenses):
    view_expenses(expenses)

    try:
        expense_id=int(input("Enter expense ID to delete : "))
    except ValueError:
        print("Invalid ID")
        return
    for expense in expenses:
        if expense["id"]==expense_id:
            expenses.remove(expense)
            save_expenses(expenses)
            print("Expense deleted.")
            return
    print("Expense not found.")

def show_menu():
    print("\nExpense Manager")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Delete expense")
    print("4. Search expense")
    print("5. Calculate total")
    print("6. Exit")


def main():
    expenses=load_expenses()

    while True:
        show_menu()
        choice=input("Choose an option : ")
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            delete_expense(expenses)
        elif choice == "4":
            search_expenses(expenses)
        elif choice == "5":
            calculate_total(expenses)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__=="__main__":
    main()