from file_handler import load_data, save_data


def add_expense():

    expenses = load_data()

    expense = {
        "id": len(expenses) + 1,
        "date": input("Enter Date: "),
        "category": input("Enter Category: "),
        "amount": float(input("Enter Amount: ")),
        "description": input("Enter Description: ")
    }

    expenses.append(expense)

    save_data(expenses)

    print("Expense Added Successfully")


def view_expenses():

    expenses = load_data()

    for expense in expenses:

        print(
            expense["id"],
            expense["date"],
            expense["category"],
            expense["amount"],
            expense["description"]
        )


def delete_expense():

    expense_id = int(input("Enter Expense ID: "))

    expenses = load_data()

    for expense in expenses:

        if expense["id"] == expense_id:

            expenses.remove(expense)

            save_data(expenses)

            print("Expense Deleted")

            return

    print("Expense Not Found")