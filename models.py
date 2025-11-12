class Category:
    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f"Category({self.name})"


class Expense:
    def __init__(self, name: str, amount: float, date: str, category: Category):
        self.name = name
        self.amount = amount
        self.date = date
        self.category = category

    def __repr__(self):
        return f"Expense({self.name},{self.amount},{self.date},{self.category.name})"
