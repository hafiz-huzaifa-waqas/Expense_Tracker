# Function to add transactions
def add_transactions(transaction):

    while True:
    
        my_dict = {}
        user_input = input("\nDo you want to add a transaction(yes/no)? : ").lower().strip()

        if user_input in ["yes", "y", "yeah"]:

            try:
                input_amount = int(input("Amount (positive value for deposit and negative for Expense): "))
                input_category = input("Category (e.g., Food, Salary, Rent, Shopping): ")
                input_description = input("Description: (Food name, Monthly Salary, Cloth shopping etc) ")
    
                my_dict["amount"] = input_amount
                my_dict["category"] = input_category
                my_dict["description"] = input_description

                transaction.append(my_dict)

            except Exception as e:
                print("Exception ", e, " occurred")

        elif user_input in ["no", "n", "nope", "nah"]:
            break

        else:
            print("Enter valid input!")
    
    return transaction


def show_summary(transactions):

    if not transactions:
        print("\nNo transactions found!\n")
        return

    # Dictionary to group amounts by category
    categories = {}
    for t in transactions:
        category = t["category"]
        if category not in categories:
            categories[category] = []
        categories[category].append(t["amount"])

    # Calculate totals
    total_income = 0
    total_expense = 0

    for category, amounts in categories.items():
        income = sum(a for a in amounts if a >= 0)
        expense = sum(abs(a) for a in amounts if a < 0)
        highest = max(amounts)
        lowest = min(amounts)
        average = sum(amounts)/len(amounts)
        
        total_income += income
        total_expense += expense

        print(f"\n======================= Summary By Category: {category} ======================\n")
        print(f"  Total Income:       ${income}")
        print(f"  Total Expense:      ${expense}")
        print(f"  Highest Transaction: ${highest}")
        print(f"  Lowest Transaction:  ${lowest}")
        print(f"  Average Transaction: ${average:.2f}")
        print("------------------------------------------------------")

    remaining = total_income - total_expense

    print("\n===================== Overall Summary ======================")
    print("Total Income:      $", total_income)
    print("Total Expense:     $", total_expense)
    print("Remaining Income:  $", remaining)
    print("============================================================")


# function to store descriptions
def get_descriptions(transactions):

    descriptions = []

    for t in transactions:
        descriptions.append(t["description"])

    return descriptions


# function to show transaction history

def show_transaction_history(transactions):

    if not transactions:
        print("\n No Transactions yet!")
        return
    
    print("\n========================= Transaction History ========================\n")

    i = 1
    for t in transactions:
        print(f"{i}. Category: {t['category']} | Amount: {t['amount']} | Description: {t['description']}")
        i+=1

    print ("\n========================================================\n")



# -------------------------------------Execution----------------------------------------------

transactions = []

while True:
    print("\n******************************** MENU ****************************\n")
    print("Choose an option:")
    print("1. Add a transaction")
    print("2. View summary")
    print("3. View Transaction History") 
    print("4. Quit")

    choice = input("Enter your choice (1/2/3): ").strip()

    if choice == "1":
        add_transactions(transactions)

    elif choice == "2":
        show_summary(transactions)

    elif choice == "3":
        show_transaction_history(transactions)


    elif choice == "4":
        print("Goodbye! Exiting the program.")
        print("\n--------------------- Terminated ------------------------\n")
        break

    else:
        print("Invalid choice! Please try again.\n")
