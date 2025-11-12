def run_menu(service):
    while True:
        print("\n=== COST ACCOUNTING MENU ===")
        print("1. Add category")
        print("2. Delete category")
        print("3. Add expense")
        print("4. Delete expense")
        print("5. List all expenses")
        print("6. Report: by name")
        print("7. Report: by date")
        print("8. Report: max expense by category")
        print("9. Report: min expense by category")
        print("10. Report: max expense in period")
        print("11. Report: min expense in period")
        print("12. Save & Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter category name: ")
            service.add_category(name)

        elif choice == "2":
            name = input("Category name to delete: ")
            service.delete_category(name)

        elif choice == "3":
            name = input("Expense name: ")
            amount = float(input("Amount: "))
            date = input("Date (YYYY-MM-DD): ")
            category = input("Category: ")
            service.add_expense(name, amount, date, category)

        elif choice == "4":
            name = input("Expense name to delete: ")
            service.delete_expense(name)

        elif choice == "5":
            service.list_expenses()

        elif choice == "6":
            name = input("Enter expense name to search: ")
            service.report_by_name(name)

        elif choice == "7":
            date = input("Enter date (YYYY-MM-DD): ")
            service.report_by_date(date)

        elif choice == "8":
            service.report_max_expense_by_category()

        elif choice == "9":
            service.report_min_expense_by_category()

        elif choice == "10":
            start = input("Start date (YYYY-MM-DD): ")
            end = input("End date (YYYY-MM-DD): ")
            service.report_max_expense_in_period(start, end)

        elif choice == "11":
            start = input("Start date (YYYY-MM-DD): ")
            end = input("End date (YYYY-MM-DD): ")
            service.report_min_expense_in_period(start, end)

        elif choice == "12":
            service.save_all()
            print("Data saved. Goodbye!")
            break

        else:
            print("Invalid choice, try again.")
