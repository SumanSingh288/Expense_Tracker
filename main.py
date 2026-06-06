from expense_manager import *
from report_manager import *

while True:

    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Total Expense")
    print("5. Highest Expense")
    print("6. Category Report")
    print("7. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        delete_expense()

    elif choice == "4":
        total_expense()

    elif choice == "5":
        highest_expense()

    elif choice == "6":
        category_report()

    elif choice == "7":
        break

    else:
        print("Invalid Choice")