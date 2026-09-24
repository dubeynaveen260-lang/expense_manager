# 💰 Expense Manager

A simple **command-line Expense Manager** built with Python.
It allows users to add, view, search, delete, and calculate expenses. All expense data is stored locally in a JSON file, so the data remains available after the program is closed.

## 📌 Features

* ➕ Add a new expense
* 👀 View all expenses
* 🔍 Search expenses by category or description
* 🗑️ Delete an expense using its ID
* 🧮 Calculate total expenses
* 💾 Automatically save expenses to a JSON file
* 📅 Automatically record the current date
* 🔄 Load previously saved expenses when the program starts

## 🛠️ Technologies Used

* **Python**
* `json` — for storing and loading expense data
* `datetime` — for recording the expense date

## 📂 Project Structure

```text
Expense-Manager/
│
├── main.py
├── expenses.json
└── README.md
```

> `expenses.json` is created automatically when the first expense is added.

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Open the project folder

```bash
cd Expense-Manager
```

### 3. Run the program

```bash
python expense_manager.py
```

## 📋 Menu

When the program starts, you will see:

```text
Expense Manager
1. Add expense
2. View expenses
3. Delete expense
4. Search expense
5. Calculate total
6. Exit
```

### 1. Add Expense

Enter:

```text
Category : Food
Amount : 250
Description : Lunch
```

The program automatically records the current date and generates an ID.

Example:

```json
{
    "id": 1,
    "category": "Food",
    "amount": 250.0,
    "date": "2026-09-24",
    "description": "Lunch"
}
```

### 2. View Expenses

Displays all saved expenses with their:

* ID
* Date
* Category
* Amount
* Description

### 3. Delete Expense

Enter the ID of the expense you want to remove.

```text
Enter expense ID to delete : 2
Expense deleted.
```

### 4. Search Expense

You can search using a category or description.

For example:

```text
Search : food
```

The program displays matching expenses.

### 5. Calculate Total

Calculates the total amount of all saved expenses.

Example:

```text
Total expenses: 1250.50
```

### 6. Exit

Closes the program.

## 💾 Data Storage

The project uses a local **`expenses.json`** file instead of a database.

Example:

```json
[
    {
        "id": 1,
        "category": "Food",
        "amount": 250.0,
        "date": "2026-09-24",
        "description": "Lunch"
    },
    {
        "id": 2,
        "category": "Travel",
        "amount": 100.0,
        "date": "2026-09-24",
        "description": "Bus fare"
    }
]
```

The program uses:

```python
json.load()
```

to read saved expenses and:

```python
json.dump()
```

to save expenses.

## 🧠 Python Concepts Used

This project demonstrates several important Python concepts:

* Functions
* Lists
* Dictionaries
* `for` loops
* `while` loops
* Conditional statements
* User input
* Exception handling with `try-except`
* List comprehensions
* JSON file handling
* File handling with `open()`
* Date and time handling
* String methods
* Formatted strings (f-strings)

## ⚠️ Current Limitations

This is a simple command-line project and does not currently include:

* User accounts
* Database storage
* Graphical interface
* Monthly reports
* Expense categories summary
* Budget limits
* Data visualization

These features can be added in future versions.

## 🚀 Future Improvements

Possible improvements include:

* Add monthly and yearly expense reports
* Add category-wise spending summaries
* Add a monthly budget feature
* Add CSV export
* Add charts and graphs
* Add a GUI
* Move from JSON to SQLite
* Add income tracking
* Add edit/update expense functionality

## 👨‍💻 Author

**Naveen Dubey**

Built as a beginner Python project to practice **file handling, JSON, functions, lists, dictionaries, and exception handling**.
