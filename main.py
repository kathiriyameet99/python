expensesList = []  # List of all expenses in dictionary form

print("Welcome to Expense Tracker: kharcha kam kiya karo 😄")

while True:
    print("\n==== MENU ====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Kharcha")
    print("4. Exit")

    choice = int(input("Please enter your choice: "))

    # 1. ADD EXPENSE
    if choice == 1:
        date = input("Kis date par kharcha kiya tha? ")
        category = input("Kis type ka kharcha kiya? (Food, Travel, Makeup, Books): ")
        description = input("Aur detail dedo: ")
        amount = float(input("Kitne ka kharcha tha: "))

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expensesList.append(expense)
        print("\nDone bro. Expense added successfully ✔")

    # 2. VIEW ALL EXPENSES
    elif choice == 2:
        if len(expensesList) == 0:
            print("No Expense Added. Jao pehle kharcha karo 😅")
        else:
            print("\n==== Ye hai aapka sara kharcha ====")
            count = 1
            for eachkharcha in expensesList:
                print(f"Kharcha {count} -> {eachkharcha['date']}, "
                      f"{eachkharcha['category']}, "
                      f"{eachkharcha['description']}, "
                      f"{eachkharcha['amount']}")
                count += 1

    # 3. VIEW TOTAL KHARCHA
    elif choice == 3:
        total = 0
        for eachkharcha in expensesList:
            total += eachkharcha["amount"]
        print("\nTOTAL KHARCHA =", total)

    # 4. EXIT
    elif choice == 4:
        print("Dhanyawad! Aapne humara system use kiya 🙏")
        break

    else:
        print("INVALID CHOICE. TRY AGAIN ❌")
