# Python Expense Tracker

A command-line expense tracker built with Python that allows users to record purchases, view expenses, and calculate total spending.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=flat)
![Status](https://img.shields.io/badge/Status-In_Development-orange?style=flat)

## Features

- Add expenses with item names and prices
- View recorded items and their amounts
- Calculate total spending automatically
- Validate empty item names and amounts
- Handle invalid expense amounts
- Navigate through an interactive menu
- Clear recorded expenses when starting a fresh session

## Built With

- **Python 3** — Main programming language
- **Lists** — Store item names and expense amounts
- **Exception Handling** — Handle invalid numeric input
- **Built-in Functions** — Calculate total spending with `sum()`

## Installation

### Clone the Repository

```bash
git clone https://github.com/bungalaowhagawatzgalow-cyber/python-expensestracker.git
cd python-expensestracker
```

### Run the Application

```bash
python expense_tracker.py
```

If needed, use `python3` instead of `python`.

## Usage

1. Start the application.
2. Choose an option from the menu.
3. Enter an item name and its price to record an expense.
4. View recorded items and their amounts.
5. Calculate the total spending.
6. Exit the application when finished.

## Example

```text
=== EXPENSE TRACKER ===

1. Add expense
2. View expenses
3. Show total spending
4. Exit

Choose an option: 1
Enter item name: Coffee
Expense amount: 3.50
Expense added!
```

## Future Improvements

- [x] Add expenses with item names and prices
- [x] View recorded expenses
- [x] Calculate total spending
- [x] Validate empty inputs
- [x] Handle invalid expense amounts
- [ ] Save expenses between sessions
- [ ] Add the ability to remove individual expenses
- [ ] Introduce expense categories
- [ ] Improve menu input validation
- [ ] Display expenses in a formatted table

## License

This project is licensed under the [MIT License](LICENSE).

---

*Built as part of my Python learning journey.*
