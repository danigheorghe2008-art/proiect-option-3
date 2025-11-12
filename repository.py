import json


class Repository:
    def __init__(self, file_path="data.json"):
        self.file_path = file_path

    def save(self, categories, expenses):
        data = {
            "categories": [cat.name for cat in categories],
            "expenses": [
                {
                    "name": exp.name,
                    "amount": exp.amount,
                    "date": exp.date,
                    "category": exp.category.name,
                }
                for exp in expenses
            ],
        }

        with open(self.file_path, "w") as f:
            json.dump(data, f, indent=2)
        print("Data saved to:", self.file_path)

    def load(self, Category, Expense):
        try:
            with open(self.file_path, "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            print("No saved data found — starting fresh.")
            return [], []

        categories = [Category(name) for name in data.get("categories", [])]
        expenses = []
        for e in data.get("expenses", []):
            cat = next((c for c in categories if c.name == e["category"]), None)
            if cat:
                expenses.append(Expense(e["name"], e["amount"], e["date"], cat))

        return categories, expenses
