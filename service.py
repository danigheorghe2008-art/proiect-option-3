from datetime import datetime


class service:
    def __init__(self, repo, Category, Expense):
        self.repo = repo
        self.Category = Category
        self.Expense = Expense
        self.categories, self.expenses = repo.load(Category, Expense)

    def add_category(self, name):
        if any(c.name == name for c in self.categories):
            print("Category already exists!!")
            return
        self.categories.append(self.Category(name))
        print("Category added!")

    def delete_category(self, name):
        self.categories = [c for c in self.categories if c.name != name]
        self.expenses = [e for e in self.expenses if e.category.name != name]
        print("Category deleted (and related expenses removed)")

    def add_expense(self, name, amount, date, category_name):
        cat = next((c for c in self.categories if c.name == category_name), None)
        if not cat:
            print("Category not found!")
            return
        self.expenses.append(self.Expense(name, amount, date, cat))
        print("Expense added!")

    def delete_expense(self, name):

        matching = [e for e in self.expenses if e.name == name]
        if not matching:
            print(f"No expense found with name '{name}'.")
            return

        self.expenses = [e for e in self.expenses if e.name != name]
        print(f"Deleted {len(matching)} expense(s) named '{name}'.")

    def list_expenses(self):
        if not self.expenses:
            print("No expenses yet.")
            return
        print("\nDate        | Name            | Amount | Category")
        print("-" * 45)
        for e in self.expenses:
            print(f"{e.date:10} | {e.name:15} | {e.amount:6.2f} | {e.category.name}")

    # REPORTS!!!

    def report_by_name(self, name):
        filtered = [e for e in self.expenses if e.name.lower() == name.lower()]
        if not filtered:
            print(f"No expenses found with name '{name}'.")
            return

        print(f"\nExpenses with name '{name}':")
        for e in filtered:
            print(f" - {e.name} ({e.amount:.2f}, {e.category.name}, {e.date})")

    def report_by_date(self, date):
        try:
            target_date = datetime.fromisoformat(date)
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD.")
            return

        filtered = [
            e
            for e in self.expenses
            if datetime.fromisoformat(e.date).date() == target_date.date()
        ]
        if not filtered:
            print(f"No expenses found on {date}.")
            return

        print(f"\nExpenses on {date}:")
        for e in filtered:
            print(f" - {e.name} ({e.amount:.2f}, {e.category.name})")

    def report_max_expense_by_category(self):
        if not self.expenses:
            print("No expenses recorded.")
            return
        max_by_cat = {}
        for e in self.expenses:
            cat = e.category.name
            if cat not in max_by_cat or e.amount > max_by_cat[cat].amount:
                max_by_cat[cat] = e
        print("\nMaximum expense in each category:")
        for cat, exp in max_by_cat.items():
            print(f" - {cat}: {exp.name} ({exp.amount:.2f} on {exp.date})")

    def report_min_expense_by_category(self):
        if not self.expenses:
            print("No expenses recorded.")
            return
        min_by_cat = {}
        for e in self.expenses:
            cat = e.category.name
            if cat not in min_by_cat or e.amount < min_by_cat[cat].amount:
                min_by_cat[cat] = e

        print("\nMinimum expense in each category:")
        for cat, exp in min_by_cat.items():
            print(f" - {cat}: {exp.name} ({exp.amount:.2f} on {exp.date})")

    def report_max_expense_in_period(self, start_date, end_date):
        if not self.expenses:
            print("No expenses yet.")
            return

        start, end = datetime.fromisoformat(start_date), datetime.fromisoformat(
            end_date
        )

        expenses_in_period = [
            e for e in self.expenses if start <= datetime.fromisoformat(e.date) <= end
        ]
        if not expenses_in_period:
            print("No expenses in this period.")
            return

        def get_amount(e):
            return e.amount

        max_expense = max(expenses_in_period, key=get_amount)

        print(f"\nMaximum expense between {start_date} and {end_date}")
        print(
            f"{max_expense.name} ({max_expense.category.name}) - {max_expense.amount}"
        )
        return max_expense

    def report_min_expense_in_period(self, start_date, end_date):

        if not self.expenses:
            print("No expenses recorded.")
            return

        start, end = datetime.fromisoformat(start_date), datetime.fromisoformat(
            end_date
        )

        in_period = [
            e for e in self.expenses if start <= datetime.fromisoformat(e.date) <= end
        ]
        if not in_period:
            print("No expenses in this period.")
            return

        def get_amount(e):
            return e.amount

        min_exp = min(in_period, key=get_amount)

        print(f"\nMinimum expense between {start_date} and {end_date}:")
        print(
            f" - {min_exp.name} ({min_exp.amount:.2f}, {min_exp.category.name}, {min_exp.date})"
        )
        return min_exp

    def save_all(self):
        self.repo.save(self.categories, self.expenses)
