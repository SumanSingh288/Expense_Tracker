from file_handler import load_data


def total_expense():

    expenses = load_data()

    total = sum(item["amount"] for item in expenses)

    print("Total Expense:", total)


def highest_expense():

    expenses = load_data()

    highest = max(expenses, key=lambda x: x["amount"])

    print(highest)


def category_report():

    category = input("Enter Category: ")

    expenses = load_data()

    for expense in expenses:

        if expense["category"].lower() == category.lower():

            print(expense)