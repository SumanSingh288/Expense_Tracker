# 💰 Expense Tracker

A Python-based Command Line Interface (CLI) application designed to track daily expenses, manage spending records, and generate financial reports. The application stores expense data in a JSON file and provides useful insights through expense analytics and reporting features.

---

## 📌 Project Overview

Expense Tracker is a personal finance management application developed using Python. It helps users record daily expenses, categorize spending, monitor financial activities, and generate reports for better budgeting and expense management.

The system follows a modular programming approach and uses JSON file handling to store expense records permanently.

---

## ✨ Features

- Add New Expenses
- View All Expenses
- Delete Expense Records
- Search Expenses by Category
- Search Expenses by Date
- Calculate Total Expenses
- View Highest Expense
- View Lowest Expense
- Category-wise Expense Reports
- Monthly Expense Summary
- JSON-Based Data Storage
- Menu Driven CLI Interface

---

## 🛠️ Technologies Used

- Python 3.x
- JSON
- VS Code
- Command Line Interface (CLI)

---

## 📂 Project Structure

```text
Expense_Tracker/
│
├── main.py
├── expense_manager.py
├── report_manager.py
├── file_handler.py
├── config.py
├── expenses.json
└── README.md
```

---

## 📊 Expense Data Structure

Each expense record contains:

- Expense ID
- Date
- Category
- Amount
- Description

Example:

```json
{
    "id": 1,
    "date": "2026-06-01",
    "category": "Food",
    "amount": 250,
    "description": "Lunch"
}
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/expense-tracker.git
```

### Navigate to Project Folder

```bash
cd expense-tracker
```

### Run the Application

```bash
python main.py
```

---

## 🚀 How to Use

After running the application, a menu will appear:

```text
========================================
         EXPENSE TRACKER
========================================

1. Add Expense
2. View Expenses
3. Delete Expense
4. Total Expense
5. Highest Expense
6. Category Report
7. Exit
```

Select an option and follow the instructions displayed on the screen.

---

## 📸 Sample Output

```text
========================================
         EXPENSE TRACKER
========================================

1. Add Expense
2. View Expenses
3. Delete Expense
4. Total Expense
5. Highest Expense
6. Category Report
7. Exit

Enter Choice: 1

Enter Date: 2026-06-20
Enter Category: Food
Enter Amount: 250
Enter Description: Lunch

Expense Added Successfully
```

---

## 📈 Reports Generated

The application can generate:

- Total Spending Report
- Highest Expense Report
- Lowest Expense Report
- Category-wise Summary
- Date-wise Expense Report
- Monthly Expense Analysis

---

## 🎯 Learning Outcomes

This project helps in understanding:

- Python Functions
- Modular Programming
- JSON File Handling
- CRUD Operations
- Data Analysis
- Report Generation
- Lists and Dictionaries
- Exception Handling
- Date and Time Handling
- CLI Development

---

## 🔮 Future Enhancements

- SQLite Database Integration
- Export Reports to CSV
- Export Reports to PDF
- Budget Planning Module
- Expense Charts and Graphs
- GUI using Tkinter
- User Authentication
- Web Version using Flask/Django

---

## 📊 Project Goals

- Track daily expenses efficiently.
- Analyze spending habits.
- Generate useful financial reports.
- Learn file handling and data management.
- Build a practical utility application using Python.

---

## 👨‍💻 Author

**SumanSingh**

Python Internship Project

---

## 📜 License

This project is developed for educational and learning purposes.
