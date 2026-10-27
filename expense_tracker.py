import time


def expensefunc():
    itemslist = []  # expnesvies
    expenses = []  # for it

    while True:  # so it doesnt stop after one choice
        print("=== EXPENSE TRACKER ===")

        print("1. Add expense")
        print("2. View expenses")
        print("3. Show total spending")
        print("4. Exit")

        chooseanoption = int(input("Choose an option: "))  # gets user choice

        if chooseanoption == 1:  # adds an expense
            item_input = input("Enter item name: ").strip()  # gets item name
            amount_input = input("Expense amount: ").strip()  # gets the price

            if not item_input or not amount_input:  # checks for empty inputs
                print("Item name and amount are required!")
            else:
                try:  # tries to convert the price into a number
                    amount = float(amount_input)
                    itemslist.append(item_input)  # adds item to list
                    expenses.append(amount)  # adds price to list
                    print("Expense added!")
                except ValueError:  # if the input isnt a number
                    print("Please enter a valid number!")

        elif chooseanoption == 2:  # views saved expenses
            print("Stuff bought:", itemslist)
            print("Amounts:", expenses)

        elif chooseanoption == 3:  # shows total spending
            print("Stuff bought:", itemslist)
            print("Total spending:", sum(expenses))  # adds all prices togther

            answer = input("Do you want to continue? (y/n): ").strip().lower()

            if answer == "y":  # after yes it will remove the data from the lists
                itemslist.clear()
                expenses.clear()
                continue
            elif answer == "n":  # exits the program
                print("Exiting...")
                time.sleep(1)
                break
            else:
                print("Please enter y or n!")

        elif chooseanoption == 4:  # exits the tracker
            print("Exiting...")
            time.sleep(1)
            break

        elif chooseanoption != 1 and chooseanoption != 2 and chooseanoption != 3 and chooseanoption != 4:
            print("Not a valid option!")  # tells the user the choice is wrong
            continue


expensefunc()  # starts the expense tracker obviously
