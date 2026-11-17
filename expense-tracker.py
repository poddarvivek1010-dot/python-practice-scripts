#Daily expense & budget tracker


class BudgetTracker:

  def __init__(self, monthly_budget):
    self.monthly_budget = monthly_budget
    self.expenses = []

  def add_expense(self, category, amount):
    if amount > 0:
      self.expenses.append({"category": category, "amount": amount})
      print(f"added: {category} - rs. {amount}")
    else:
      print("expense amount must be greater than zero.")

  def total_spent(self):
    return sum(item["amount"] for item in self.expenses)

  def show_summary(self):
    spent = self.total_spent()
    remaining = self.monthly_budget - spent
    print("\nMonthly budget summary....")
    print(f"total budget : rs. {self.monthly_budget}")
    print(f"Total spent  : rs. {spent}")
    print(f"Remaining    : rs. {remaining}")
    if remaining < 0:
      print("alert: monthly budget exceeded!")


#sample outcomes
tracker = BudgetTracker(5000)
tracker.add_expense("groceries", 1450)
tracker.add_expense("internet", 625)
tracker.add_expense("books", 872)
tracker.show_summary()
